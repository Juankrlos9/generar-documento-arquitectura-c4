from fpdf import FPDF
import datetime

class SAD_PDF(FPDF):
    def header(self):
        # Encabezado corporativo
        self.set_font('Arial', 'B', 10)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, 'Documento de Definición de Arquitectura (SAD) - CCS NextGen', 0, 1, 'R')
        self.line(10, 20, 200, 20)
        self.ln(15)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Página {self.page_no()} | Confidencial', 0, 0, 'C')

    def chapter_title(self, num, label):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(0, 51, 102) # Azul oscuro
        self.cell(0, 10, f'{num}. {label}', 0, 1, 'L')
        self.ln(5)
        self.set_text_color(0, 0, 0) # Reset a negro

    def chapter_body(self, text):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 6, text)
        self.ln()

    def add_section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 8, title, 0, 1, 'L', 1)
        self.ln(3)

    def add_bullet_point(self, text):
        self.set_font('Arial', '', 11)
        self.cell(10) # Sangría
        self.cell(5, 6, chr(149), 0, 0) # Bullet char
        self.multi_cell(0, 6, text)
        self.ln(2)

    def add_image_box(self, image_path, caption):
        self.ln(5)
        try:
            # Centrar imagen
            x_centered = (210 - 170) / 2
            self.image(image_path, x=x_centered, w=170)
            self.ln(2)
            self.set_font('Arial', 'I', 9)
            self.set_text_color(100)
            self.cell(0, 5, caption, 0, 1, 'C')
            self.set_text_color(0)
        except Exception:
            self.set_font('Arial', 'B', 10)
            self.set_text_color(255, 0, 0)
            self.cell(0, 10, f"[Imagen no encontrada: {image_path}]", 0, 1, 'C')
            self.set_text_color(0)
        self.ln(10)

def generate_detailed_pdf():
    pdf = SAD_PDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    # --- PORTADA ---
    pdf.ln(60)
    pdf.set_font('Arial', 'B', 26)
    pdf.set_text_color(0, 51, 102)
    pdf.multi_cell(0, 10, 'Documento de Arquitectura de Software\nPlataforma CCS NextGen', 0, 'C')
    pdf.ln(20)
    
    pdf.set_font('Arial', '', 14)
    pdf.set_text_color(0)
    pdf.cell(0, 10, 'Cliente: Compañía Colombiana de Seguimiento', 0, 1, 'C')
    pdf.cell(0, 10, f'Fecha: {datetime.date.today()}', 0, 1, 'C')
    pdf.cell(0, 10, 'Versión: 2.0 (Detallada)', 0, 1, 'C')
    
    pdf.add_page()

    # --- 1. VISIÓN GENERAL ---
    pdf.chapter_title('1', 'Visión General y Objetivos')
    pdf.chapter_body(
        "El presente documento detalla la arquitectura de referencia para la modernización tecnológica de CCS. "
        "El objetivo principal es soportar la ingesta masiva de datos IoT provenientes de la flota de vehículos "
        "y digitalizar el proceso comercial."
    )
    pdf.add_section_title("Retos de Negocio:")
    pdf.add_bullet_point("Procesar picos de carga de 5000 señales por segundo.")
    pdf.add_bullet_point("Garantizar latencia crítica (< 2s) para alertas de botón de pánico.")
    pdf.add_bullet_point("Implementar flujo de aprobación para contratos mayores a 50 vehículos.")
    pdf.add_bullet_point("Proveer análisis histórico (Plan Plus) mediante Big Data.")

    # --- 2. C4 NIVEL 1 ---
    pdf.chapter_title('2', 'Vista de Contexto (C4 Nivel 1)')
    pdf.chapter_body(
        "El diagrama de contexto ilustra las fronteras del sistema. Se destaca la interacción con los sensores físicos "
        "del camión, los actores humanos (Conductor, Cliente, Manager) y las dependencias externas críticas como el "
        "validador de identidad y el proveedor de SMS."
    )
    pdf.add_image_box('diagrama_contexto.png', 'Figura 1: Diagrama de Contexto del Sistema CCS')

    # --- 3. C4 NIVEL 2 ---
    pdf.chapter_title('3', 'Vista de Contenedores (C4 Nivel 2)')
    pdf.chapter_body(
        "Esta vista desglosa la solución en unidades desplegables y ejecutables. Se ha aplicado el patrón CQRS "
        "para segregar la carga transaccional (Ventas) de la carga de telemetría (IoT)."
    )
    pdf.add_image_box('diagrama_contenedores.png', 'Figura 2: Arquitectura de Contenedores y Microservicios')
    
    pdf.add_section_title("Descripción de Subsistemas:")
    pdf.add_bullet_point("Canales Digitales: Aplicaciones SPA y Mobile desacopladas del backend.")
    pdf.add_bullet_point("IoT Core (Hot Path): Broker MQTT y Kafka para ingesta de alta velocidad.")
    pdf.add_bullet_point("Business Core: Microservicios para gestión de contratos y facturación.")

    # --- 4. STACK TECNOLÓGICO ---
    pdf.chapter_title('4', 'Definición del Stack Tecnológico')
    pdf.chapter_body("A continuación, se justifican las tecnologías seleccionadas para cada capa de la arquitectura:")
    
    # Tabla simulada con celdas
    col_w = [50, 60, 80] # Anchos
    headers = ['Capa', 'Tecnología', 'Justificación']
    data = [
        ['Frontend Web', 'React.js', 'Componentización, ecosistema rico y performance en cliente (SPA).'],
        ['Mobile App', 'Flutter', 'Desarrollo híbrido eficiente (iOS/Android) con un solo código base.'],
        ['Backend (Negocio)', 'Java / Spring Boot', 'Robustez empresarial, facilidad de integración y amplia disponibilidad de talento.'],
        ['Ingesta IoT', 'Go (Golang)', 'Manejo eficiente de concurrencia para procesar miles de conexiones MQTT.'],
        ['Message Broker', 'Apache Kafka', 'Buffer persistente necesario para "aplanar" la curva de 5000 req/s.'],
        ['Base de Datos (IoT)', 'InfluxDB', 'Base de datos de series de tiempo optimizada para escrituras masivas (Append-only).'],
        ['Base de Datos (Core)', 'PostgreSQL', 'Consistencia ACID para transacciones financieras y datos de clientes.'],
        ['Infraestructura', 'Kubernetes (K8s)', 'Orquestación de contenedores para auto-escalado elástico en picos de carga.']
    ]
    
    pdf.set_font('Arial', 'B', 10)
    pdf.set_fill_color(200, 220, 255)
    for i, h in enumerate(headers):
        pdf.cell(col_w[i], 7, h, 1, 0, 'C', 1)
    pdf.ln()
    
    pdf.set_font('Arial', '', 10)
    for row in data:
        # Calcular altura máxima de la fila
        pdf.cell(col_w[0], 14, row[0], 1)
        pdf.cell(col_w[1], 14, row[1], 1)
        # Multi-cell simulado para la justificación
        x = pdf.get_x()
        y = pdf.get_y()
        pdf.multi_cell(col_w[2], 7, row[2], 1)
        pdf.set_xy(x + col_w[2], y) # Volver a la derecha
        pdf.ln(14) # Moverse al final de la fila (ajuste manual simplificado)

    # --- 5. ATRIBUTOS DE CALIDAD ---
    pdf.add_page()
    pdf.chapter_title('5', 'Atributos de Calidad (ASR)')
    
    pdf.add_section_title("5.1 Rendimiento y Escalabilidad")
    pdf.chapter_body(
        "Para cumplir con el requisito de 5000 señales/seg, la arquitectura no escribe directamente en base de datos. "
        "Utiliza un enfoque Event-Driven donde Kafka actúa como buffer. Los consumidores (Stream Processors) pueden "
        "escalar horizontalmente (HPA en Kubernetes) basándose en la métrica de 'Consumer Lag'."
    )
    
    pdf.add_section_title("5.2 Disponibilidad y Resiliencia")
    pdf.chapter_body(
        "El sistema separa el 'Camino Crítico' (Pánico) del 'Camino Normal' (Telemetría). Si la base de datos de reportes falla, "
        "el módulo de alertas sigue funcionando en memoria. Despliegue Multi-AZ (Zona de Disponibilidad) asegura continuidad "
        "ante fallos de datacenter."
    )
    
    pdf.add_section_title("5.3 Seguridad")
    pdf.add_bullet_point("Tránsito: TLS 1.2+ obligatorio para sensores y clientes.")
    pdf.add_bullet_point("Autenticación Sensores: Certificados mTLS (Mutual TLS) por dispositivo.")
    pdf.add_bullet_point("Autenticación Usuarios: OAuth2 / OpenID Connect.")
    
    # --- 6. DETALLE DE COMPONENTES ---
    pdf.chapter_title('6', 'Detalle de Componentes Críticos (C4 Nivel 3)')
    pdf.chapter_body(
        "Se detalla el funcionamiento interno del 'Stream Processor', el componente más complejo del sistema:"
    )
    pdf.add_bullet_point("Dispatcher: Recibe el evento de Kafka y lee la cabecera 'Type'.")
    pdf.add_bullet_point("Panic Handler: Si Type='PANIC', invoca inmediatamente al API de Notificaciones (Twilio/SendGrid).")
    pdf.add_bullet_point("Metrics Aggregator: Si Type='GPS', guarda en memoria (Windowing 5 min) y escribe en lote a InfluxDB.")
    
    # Intento de agregar diagrama de componentes si existe
    pdf.add_image_box('diagrama_componentes.png', 'Figura 3: Diagrama de Componentes (Stream Processor)')

    # Salida
    output_filename = 'SAD_CCS_Detailed_Architecture.pdf'
    pdf.output(output_filename)
    print(f"PDF generado exitosamente: {output_filename}")
    

if __name__ == '__main__':
    generate_detailed_pdf()