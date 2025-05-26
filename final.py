import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import cm

def check_dependencies():
    try:
        import numpy
        import skfuzzy
        import matplotlib
    except ImportError as e:
        print("Eksik bağımlılıklar tespit edildi. Lütfen şu komutu çalıştırın:")
        print("pip install -r requirements.txt")
        raise e


class TireMaintenanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lastik Bakım Analiz Sistemi")
        self.root.geometry("1200x800")
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.configure_styles()
        
        self.create_fuzzy_system()
        self.setup_ui()
        
    def configure_styles(self):
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Helvetica', 10))
        self.style.configure('TButton', font=('Helvetica', 10), padding=5)
        self.style.configure('Header.TLabel', font=('Helvetica', 12, 'bold'))
        self.style.configure('Result.TLabel', font=('Helvetica', 11, 'bold'))
        self.style.configure('H1.TLabel', font=('Helvetica', 14, 'bold'), foreground='#2c3e50')
        self.style.configure('H2.TLabel', font=('Helvetica', 12, 'bold'), foreground='#34495e')
        self.style.configure('Input.TFrame', background='#e8f4f8', relief=tk.RAISED, borderwidth=1)
        self.style.configure('Output.TFrame', background='#e8f8f0', relief=tk.RAISED, borderwidth=1)
        self.style.configure('Graph.TFrame', background='#ffffff', relief=tk.SUNKEN, borderwidth=1)
        self.style.map('TButton',
                      foreground=[('pressed', 'white'), ('active', 'white')],
                      background=[('pressed', '#2980b9'), ('active', '#3498db')])
    
    def create_fuzzy_system(self):
        # Girdiler
        self.usage_time = ctrl.Antecedent(np.arange(0, 11, 1), 'usage_time')
        self.road_type = ctrl.Antecedent(np.arange(0, 11, 1), 'road_type')
        self.temperature = ctrl.Antecedent(np.arange(-10, 51, 1), 'temperature')
        self.average_speed = ctrl.Antecedent(np.arange(0, 181, 1), 'average_speed')
        self.tire_pressure = ctrl.Antecedent(np.arange(20, 41, 1), 'tire_pressure')

        # Çıktılar
        self.maintenance_priority = ctrl.Consequent(np.arange(0, 11, 1), 'maintenance_priority')
        self.change_probability = ctrl.Consequent(np.arange(0, 101, 1), 'change_probability')

        # Üyelik fonksiyonları - Girdiler
        self.usage_time['low'] = fuzz.trimf(self.usage_time.universe, [0, 0, 3])
        self.usage_time['medium'] = fuzz.trimf(self.usage_time.universe, [2, 5, 8])
        self.usage_time['high'] = fuzz.trimf(self.usage_time.universe, [6, 10, 10])

        self.road_type['soft'] = fuzz.trimf(self.road_type.universe, [0, 0, 3])
        self.road_type['medium'] = fuzz.trimf(self.road_type.universe, [2, 5, 8])
        self.road_type['hard'] = fuzz.trimf(self.road_type.universe, [6, 10, 10])

        self.temperature['cold'] = fuzz.trimf(self.temperature.universe, [-10, -10, 10])
        self.temperature['moderate'] = fuzz.trimf(self.temperature.universe, [5, 20, 30])
        self.temperature['hot'] = fuzz.trimf(self.temperature.universe, [25, 50, 50])

        self.average_speed['slow'] = fuzz.trimf(self.average_speed.universe, [0, 0, 60])
        self.average_speed['moderate'] = fuzz.trimf(self.average_speed.universe, [40, 90, 140])
        self.average_speed['fast'] = fuzz.trimf(self.average_speed.universe, [120, 180, 180])

        self.tire_pressure['low'] = fuzz.trimf(self.tire_pressure.universe, [20, 20, 28])
        self.tire_pressure['optimal'] = fuzz.trimf(self.tire_pressure.universe, [26, 30, 34])
        self.tire_pressure['high'] = fuzz.trimf(self.tire_pressure.universe, [32, 40, 40])

        # Üyelik fonksiyonları - Çıktılar
        self.maintenance_priority['low'] = fuzz.trimf(self.maintenance_priority.universe, [0, 0, 3])
        self.maintenance_priority['medium'] = fuzz.trimf(self.maintenance_priority.universe, [2, 5, 8])
        self.maintenance_priority['high'] = fuzz.trimf(self.maintenance_priority.universe, [7, 10, 10])

        self.change_probability['low'] = fuzz.trimf(self.change_probability.universe, [0, 0, 30])
        self.change_probability['medium'] = fuzz.trimf(self.change_probability.universe, [20, 50, 80])
        self.change_probability['high'] = fuzz.trimf(self.change_probability.universe, [70, 100, 100])

        # Kurallar
        self.rules = [
            {
                'rule': ctrl.Rule(self.usage_time['high'] & self.road_type['hard'], self.maintenance_priority['high']),
                'desc': "Eğer kullanım süresi yüksek VE yol sert ise, bakım önceliği yüksektir.",
                'weight': 1.0
            },
            {
                'rule': ctrl.Rule(self.usage_time['medium'] & self.road_type['medium'], self.maintenance_priority['medium']),
                'desc': "Eğer kullanım süresi orta VE yol orta sertlikte ise, bakım önceliği ortadır.",
                'weight': 1.0
            },
            {
                'rule': ctrl.Rule(self.usage_time['low'] & self.road_type['soft'], self.maintenance_priority['low']),
                'desc': "Eğer kullanım süresi düşük VE yol yumuşak ise, bakım önceliği düşüktür.",
                'weight': 1.0
            },
            {
                'rule': ctrl.Rule(self.average_speed['fast'] | self.temperature['hot'] | self.tire_pressure['low'], self.change_probability['high']),
                'desc': "Eğer ortalama hız yüksek VEYA sıcaklık yüksek VEYA lastik basıncı düşük ise, değişim ihtimali yüksektir.",
                'weight': 1.0
            },
            {
                'rule': ctrl.Rule(self.average_speed['moderate'] & self.tire_pressure['optimal'], self.change_probability['medium']),
                'desc': "Eğer ortalama hız orta VE lastik basıncı optimal ise, değişim ihtimali ortadır.",
                'weight': 1.0
            },
            {
                'rule': ctrl.Rule(self.average_speed['slow'] & self.tire_pressure['optimal'], self.change_probability['low']),
                'desc': "Eğer ortalama hız düşük VE lastik basıncı optimal ise, değişim ihtimali düşüktür.",
                'weight': 1.0
            },
            {
                'rule': ctrl.Rule(self.temperature['cold'] & self.tire_pressure['high'], self.maintenance_priority['medium']),
                'desc': "Eğer sıcaklık düşük VE lastik basıncı yüksek ise, bakım önceliği ortadır.",
                'weight': 1.0
            },
            {
                'rule': ctrl.Rule(self.usage_time['high'] & self.tire_pressure['low'], self.change_probability['high']),
                'desc': "Eğer kullanım süresi yüksek VE lastik basıncı düşük ise, değişim ihtimali yüksektir.",
                'weight': 1.0
            }
        ]
        
        # Kontrol sistemi
        self.control_system = ctrl.ControlSystem([r['rule'] for r in self.rules])
        self.simulation = ctrl.ControlSystemSimulation(self.control_system)
        
        # Varsayılan değerler
        self.default_values = {
            'usage_time': 5,
            'road_type': 5,
            'temperature': 20,
            'average_speed': 90,
            'tire_pressure': 30
        }
    
    def setup_ui(self):
        # Ana çerçeveler
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        self.input_frame = ttk.Frame(self.main_frame, style='Input.TFrame', padding="10")
        self.input_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.output_frame = ttk.Frame(self.main_frame, style='Output.TFrame', padding="10")
        self.output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Giriş kontrolleri
        self.create_input_controls()
        
        # Çıkış kontrolleri
        self.create_output_controls()
        
        # Grafik alanı
        self.create_graph_area()
        
        # Varsayılan değerleri yükle
        self.load_default_values()
    
    def create_input_controls(self):
        # Başlık
        ttk.Label(self.input_frame, text="Lastik Kullanım Parametreleri", style='H1.TLabel').grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # Giriş alanları
        self.create_slider_input("Günlük Kullanım Süresi (saat):", 'usage_time', 0, 10, 1, 1)
        self.create_slider_input("Yol Sertliği (0: çok yumuşak, 10: çok sert):", 'road_type', 0, 10, 1, 2)
        self.create_slider_input("Ortam Sıcaklığı (°C):", 'temperature', -10, 50, 1, 3)
        self.create_slider_input("Ortalama Hız (km/s):", 'average_speed', 0, 180, 5, 4)
        self.create_slider_input("Lastik Basıncı (PSI):", 'tire_pressure', 20, 40, 1, 5)
        
        # Butonlar
        button_frame = ttk.Frame(self.input_frame)
        button_frame.grid(row=6, column=0, columnspan=2, pady=10)
        
        ttk.Button(button_frame, text="Hesapla", command=self.calculate).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Varsayılanlar", command=self.load_default_values).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Üyelik Fonksiyonları", command=self.show_membership_functions).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Kurallar", command=self.show_rules).pack(side=tk.LEFT, padx=5)
    
    def create_slider_input(self, label_text, variable_name, from_, to, resolution, row):
        label = ttk.Label(self.input_frame, text=label_text)
        label.grid(row=row, column=0, sticky=tk.W, pady=2)
        
        current_value = tk.DoubleVar(value=self.default_values[variable_name])
        setattr(self, f"{variable_name}_var", current_value)
        
        slider = ttk.Scale(self.input_frame, from_=from_, to=to, variable=current_value, 
                          orient=tk.HORIZONTAL, length=300, command=lambda v: self.update_slider_value(variable_name, v))
        slider.grid(row=row, column=1, sticky=tk.W, padx=5)
        
        value_label = ttk.Label(self.input_frame, text=f"{current_value.get():.1f}")
        value_label.grid(row=row, column=2, padx=5)
        setattr(self, f"{variable_name}_label", value_label)
        
        # Çözünürlük ayarı
        slider.configure(command=lambda v: self.update_slider_value(variable_name, v, resolution))
    
    def update_slider_value(self, variable_name, value, resolution=1):
        rounded_value = round(float(value) / resolution) * resolution
        getattr(self, f"{variable_name}_var").set(rounded_value)
        getattr(self, f"{variable_name}_label").config(text=f"{rounded_value:.1f}")
    
    def create_output_controls(self):
        # Başlık
        ttk.Label(self.output_frame, text="Analiz Sonuçları", style='H1.TLabel').grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        # Sonuçlar
        ttk.Label(self.output_frame, text="Bakım Önceliği:", style='H2.TLabel').grid(row=1, column=0, sticky=tk.W, pady=5)
        self.maintenance_result = ttk.Label(self.output_frame, text="-", style='Result.TLabel')
        self.maintenance_result.grid(row=1, column=1, sticky=tk.W, padx=5)
        
        ttk.Label(self.output_frame, text="Değişim İhtimali:", style='H2.TLabel').grid(row=2, column=0, sticky=tk.W, pady=5)
        self.change_result = ttk.Label(self.output_frame, text="-", style='Result.TLabel')
        self.change_result.grid(row=2, column=1, sticky=tk.W, padx=5)
        
        # Açıklama
        ttk.Label(self.output_frame, text="Sonuç Açıklaması:", style='H2.TLabel').grid(row=3, column=0, sticky=tk.W, pady=5)
        self.result_explanation = tk.Text(self.output_frame, height=15, width=60, wrap=tk.WORD, font=('Helvetica', 9))
        self.result_explanation.grid(row=4, column=0, columnspan=2, sticky=tk.W+tk.E, pady=5)
        
        # Grafik butonları
        graph_button_frame = ttk.Frame(self.output_frame)
        graph_button_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        ttk.Button(graph_button_frame, text="Bakım Önceliği Grafiği", command=lambda: self.show_output_graph('maintenance_priority')).pack(side=tk.LEFT, padx=2)
        ttk.Button(graph_button_frame, text="Değişim İhtimali Grafiği", command=lambda: self.show_output_graph('change_probability')).pack(side=tk.LEFT, padx=2)
    
    def create_graph_area(self):
        self.graph_frame = ttk.Frame(self.root, style='Graph.TFrame', padding="10")
        self.graph_frame.pack(fill=tk.BOTH, expand=True)
        
        self.figure = Figure(figsize=(20, 10), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.graph_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Başlangıçta boş bir grafik göster
        self.clear_graph()
    
    def clear_graph(self):
        self.figure.clear()
        self.canvas.draw()
    
    def load_default_values(self):
        for var_name, value in self.default_values.items():
            getattr(self, f"{var_name}_var").set(value)
            getattr(self, f"{var_name}_label").config(text=f"{value:.1f}")
    
    def calculate(self):
        try:
            # Girdileri al
            inputs = {
                'usage_time': self.usage_time_var.get(),
                'road_type': self.road_type_var.get(),
                'temperature': self.temperature_var.get(),
                'average_speed': self.average_speed_var.get(),
                'tire_pressure': self.tire_pressure_var.get()
            }
            
            # Hesaplamayı yap
            self.simulation.input['usage_time'] = inputs['usage_time']
            self.simulation.input['road_type'] = inputs['road_type']
            self.simulation.input['temperature'] = inputs['temperature']
            self.simulation.input['average_speed'] = inputs['average_speed']
            self.simulation.input['tire_pressure'] = inputs['tire_pressure']
            
            self.simulation.compute()
            
            # Sonuçları göster
            maintenance_val = self.simulation.output['maintenance_priority']
            change_val = self.simulation.output['change_probability']
            
            self.maintenance_result.config(text=f"{maintenance_val:.2f} - {self.get_priority_level(maintenance_val)}")
            self.change_result.config(text=f"{change_val:.2f}% - {self.get_probability_level(change_val)}")
            
            # Açıklama oluştur
            explanation = self.generate_explanation(inputs, maintenance_val, change_val)
            self.result_explanation.delete(1.0, tk.END)
            self.result_explanation.insert(tk.END, explanation)
            
            # Bakım önceliği grafiğini göster
            self.show_output_graph('maintenance_priority')
            
        except Exception as e:
            self.result_explanation.delete(1.0, tk.END)
            self.result_explanation.insert(tk.END, f"Hata oluştu: {str(e)}")
    
    def get_priority_level(self, value):
        if value <= 3:
            return "Düşük Öncelik"
        elif value <= 7:
            return "Orta Öncelik"
        else:
            return "Yüksek Öncelik"
    
    def get_probability_level(self, value):
        if value <= 30:
            return "Düşük İhtimal"
        elif value <= 70:
            return "Orta İhtimal"
        else:
            return "Yüksek İhtimal"
    
    def generate_explanation(self, inputs, maintenance_val, change_val):
        explanation = "Girilen Parametreler:\n"
        explanation += f"- Günlük Kullanım Süresi: {inputs['usage_time']} saat\n"
        explanation += f"- Yol Sertliği: {inputs['road_type']}/10\n"
        explanation += f"- Ortam Sıcaklığı: {inputs['temperature']}°C\n"
        explanation += f"- Ortalama Hız: {inputs['average_speed']} km/s\n"
        explanation += f"- Lastik Basıncı: {inputs['tire_pressure']} PSI\n\n"
        
        explanation += "Sonuç Analizi:\n"
        
        # Bakım önceliği açıklaması
        if maintenance_val >= 7:
            explanation += "🔴 Yüksek bakım önceliği tespit edildi. Lastikleriniz yoğun kullanım, sert yol koşulları veya uygun olmayan basınç nedeniyle hızlı aşınıyor olabilir. En kısa sürede kontrol edilmesi önerilir.\n\n"
        elif maintenance_val >= 3:
            explanation += "🟡 Orta seviyede bakım önceliği tespit edildi. Lastikleriniz normalden biraz daha hızlı aşınıyor olabilir. Önümüzdeki haftalar içinde kontrol edilmesi uygun olacaktır.\n\n"
        else:
            explanation += "🟢 Düşük bakım önceliği tespit edildi. Lastikleriniz normal koşullarda aşınıyor. Rutin bakım programınıza devam edebilirsiniz.\n\n"
        
        # Değişim ihtimali açıklaması
        if change_val >= 70:
            explanation += f"⚠️ Değişim ihtimali %{change_val:.0f} (Yüksek). Lastikleriniz kısa sürede değişim gerektirebilir. Detaylı inceleme yapılması önerilir.\n"
        elif change_val >= 30:
            explanation += f"ℹ️ Değişim ihtimali %{change_val:.0f} (Orta). Lastikleriniz normal aşınma sürecinde olabilir. Periyodik kontrolleri aksatmayın.\n"
        else:
            explanation += f"✅ Değişim ihtimali %{change_val:.0f} (Düşük). Lastikleriniz iyi durumda görünüyor. Düzenli kontrollerle bu durumu sürdürebilirsiniz.\n"
        
        return explanation
    
    def show_output_graph(self, output_var):
        self.figure.clear()
        
        if output_var == 'maintenance_priority':
            var = self.maintenance_priority
            title = "Bakım Önceliği Üyelik Fonksiyonları ve Sonuç"
            output_value = self.simulation.output.get('maintenance_priority', 0)
        else:
            var = self.change_probability
            title = "Değişim İhtimali Üyelik Fonksiyonları ve Sonuç"
            output_value = self.simulation.output.get('change_probability', 0)
        
        ax = self.figure.add_subplot(111)
        
        # Üyelik fonksiyonlarını çiz
        for term in var.terms:
            ax.plot(var.universe, fuzz.interp_membership(var.universe, var[term].mf, var.universe), 
                   linewidth=1.5, label=term)
        
        # Sonucu işaretle
        if output_value > 0:
            # Aktivasyon seviyelerini hesapla
            activations = {}
            for term in var.terms:
                activations[term] = fuzz.interp_membership(var.universe, var[term].mf, output_value)
            
            # En yüksek aktivasyonu bul
            max_activation_term = max(activations, key=activations.get)
            max_activation = activations[max_activation_term]
            
            # Sonucu çiz
            ax.vlines(output_value, 0, max_activation, color='k', linestyle='--', linewidth=2)
            ax.plot(output_value, max_activation, 'ko', markersize=8)
            ax.annotate(f'Sonuç: {output_value:.2f}', 
                       xy=(output_value, max_activation), 
                       xytext=(output_value+5, max_activation+0.1),
                       arrowprops=dict(facecolor='black', shrink=0.05))
            
            # Alanları doldur
            for term in var.terms:
                activation = fuzz.interp_membership(var.universe, var[term].mf, output_value)
                if activation > 0:
                    ax.fill_between(var.universe, 0, 
                                   np.fmin(var[term].mf, activation), 
                                   alpha=0.3)
        
        ax.set_title(title)
        ax.legend()
        ax.set_ylim(0, 1.1)
        ax.grid(True)
        
        self.canvas.draw()
    
    def show_membership_functions(self):
        top = tk.Toplevel(self.root)
        top.title("Üyelik Fonksiyonları")
        top.geometry("1000x700")
        
        notebook = ttk.Notebook(top)
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Girdi fonksiyonları
        input_frame = ttk.Frame(notebook)
        notebook.add(input_frame, text="Girdi Fonksiyonları")
        
        fig_input = Figure(figsize=(10, 8), dpi=100)
        canvas_input = FigureCanvasTkAgg(fig_input, master=input_frame)
        canvas_input.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Girdi fonksiyonlarını çiz
        ax1 = fig_input.add_subplot(321)
        self.plot_membership(self.usage_time, ax1, "Günlük Kullanım Süresi (saat)")
        
        ax2 = fig_input.add_subplot(322)
        self.plot_membership(self.road_type, ax2, "Yol Sertliği")
        
        ax3 = fig_input.add_subplot(323)
        self.plot_membership(self.temperature, ax3, "Sıcaklık (°C)")
        
        ax4 = fig_input.add_subplot(324)
        self.plot_membership(self.average_speed, ax4, "Ortalama Hız (km/s)")
        
        ax5 = fig_input.add_subplot(325)
        self.plot_membership(self.tire_pressure, ax5, "Lastik Basıncı (PSI)")
        
        fig_input.tight_layout()
        canvas_input.draw()
        
        # Çıktı fonksiyonları
        output_frame = ttk.Frame(notebook)
        notebook.add(output_frame, text="Çıktı Fonksiyonları")
        
        fig_output = Figure(figsize=(10, 4), dpi=100)
        canvas_output = FigureCanvasTkAgg(fig_output, master=output_frame)
        canvas_output.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Çıktı fonksiyonlarını çiz
        ax6 = fig_output.add_subplot(121)
        self.plot_membership(self.maintenance_priority, ax6, "Bakım Önceliği")
        
        ax7 = fig_output.add_subplot(122)
        self.plot_membership(self.change_probability, ax7, "Değişim İhtimali (%)")
        
        fig_output.tight_layout()
        canvas_output.draw()
    
    def plot_membership(self, var, ax, title):
        for term in var.terms:
            ax.plot(var.universe, var[term].mf, linewidth=1.5, label=term)
        
        ax.set_title(title)
        ax.legend()
        ax.grid(True)
        ax.set_ylim(0, 1.1)
    
    def show_rules(self):
        top = tk.Toplevel(self.root)
        top.title("Kurallar ve Açıklamaları")
        top.geometry("1200x900")
        
        main_frame = ttk.Frame(top)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Başlık
        ttk.Label(main_frame, text="Fuzzy Mantık Kuralları", style='H1.TLabel').pack(pady=10)
        
        # Canvas ve Scrollbar oluştur
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Kuralları ekleme
        for i, rule in enumerate(self.rules):
            rule_frame = ttk.Frame(scrollable_frame, relief=tk.RAISED, borderwidth=1, padding=10)
            rule_frame.pack(fill=tk.X, pady=5, padx=5)
            
            # Kural numarası
            ttk.Label(rule_frame, text=f"Kural {i+1}:", style='H2.TLabel').grid(row=0, column=0, sticky=tk.W)
            
            # Kural ifadesi
            ttk.Label(rule_frame, text=str(rule['rule']), wraplength=1000, justify=tk.LEFT).grid(
                row=1, column=0, sticky=tk.W, pady=5)
            
            # Açıklama başlığı
            ttk.Label(rule_frame, text="Açıklama:", style='H2.TLabel').grid(
                row=2, column=0, sticky=tk.W, pady=(10, 0))
            
            # Açıklama metni
            ttk.Label(rule_frame, text=rule['desc'], wraplength=1000, justify=tk.LEFT).grid(
                row=3, column=0, sticky=tk.W)
                                    
            # Grid yapılandırması
            rule_frame.grid_columnconfigure(0, weight=1)
        
        # Scrollable frame'i güncelle
        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
    
if __name__ == "__main__":
    check_dependencies()
    root = tk.Tk()
    app = TireMaintenanceApp(root)
    root.mainloop()