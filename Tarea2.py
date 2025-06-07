### TAREA 2 CLASES Y HERENCIA ###
### HUGO NÚÑEZ PECHUANTE ###

'''PARTE 1 DEFINICION DE CLASES'''
print("\n")
print("PARTE 1")
print("\n")


class Explosives:  # Creamos la clase explosivos
    """
    Clase que representa un explosivo.

    Atributos:
    ----------
    commercial_name : str
        Nombre comercial del explosivo.
    explosive_density : float
        Densidad del explosivo en g/cm³.
    vod : int
        Velocidad de detonación (VoD) en m/s.
    rws : float
        Fuerza relativa respecto al ANFO (Relative Weight Strength).
    water_resistance : str
        Indicador de resistencia al agua, colocar 'Si' o 'No'.

    Métodos:
    ---------
    detonation_pressure():
        Calcula y muestra la presión de detonación del explosivo usando la fórmula:
        P = (1/4) * densidad * VoD²

    linear_density(diameter_mm: float):
        Calcula y muestra la densidad lineal del explosivo en función del diámetro (en mm)
        usando la fórmula: (π/4) * diámetro² * densidad

    kg_anfo_equivalent(weight_explosive: float):
        Calcula y muestra el equivalente en kg de ANFO para un peso dado de explosivo.

    is_for_water():
        Indica si el explosivo es o no resistente al agua.
    """

    def __init__(
            self, commercial_name,
            explosive_density,
            vod, rws,  # Relative Weight Strengh
            water_resistance):

        self.commercial_name = commercial_name
        self.explosive_density = explosive_density
        self.vod = vod
        self.rws = rws
        self.water_resistance = water_resistance
        return

# Realizamos los calculos
    def detonation_pressure(self):
        presideton = (1/4)*self.explosive_density*self.vod**2
        print(
            f"La presion de detonacion del explosivo {self.commercial_name} es: {presideton} kPa")
        return

    def linear_density(self, diameter_mm):
        densilin = (3.1416/4)*diameter_mm**2*self.explosive_density
        print(
            f"Considerando un diametro de {diameter_mm} mm, la densidad lineal del explosivo {self.commercial_name} es: {densilin} kilogramos por metro")
        return

    def kg_anfo_equivalent(self, weight_explosive):
        kg_ANFO = (self.rws*weight_explosive)
        print(
            f"500 kilogramos del explosivo {self.commercial_name} equivalen a {kg_ANFO} kg de ANFO")
        return

    def is_for_water(self):
        if self.water_resistance == 'Si':
            print(
                f"El explosivo {self.commercial_name} Sí es resistente al agua")
        elif self.water_resistance == 'No':
            print("El explosivo No es resitente al agua")
        return


# CREACION DE 2 EXPLOSIVOS

# Instanciar pasando los valores iniciales :
Explosive_1 = Explosives('Tronex Plus', 1.18, 5200, 1.22, 'Si')

# Crear una segunda instancia:
Explosive_2 = Explosives('Emultex CP', 1.15, 4400, 0.89, 'Si')

# a) Calcular las presiones de detonación
Explosive_1.detonation_pressure()
Explosive_2.detonation_pressure()
print("\n")

# b) Densidad lineal para diametro de 140 mm
Explosive_1.linear_density(140)
Explosive_2.linear_density(140)
print("\n")

# c) A cuántos kg de ANFO equivalen 500 kg del explosivo
Explosive_1.kg_anfo_equivalent(500)
Explosive_2.kg_anfo_equivalent(500)
print("\n")

# d) ¿Los explosivos son resistentes al agua?
Explosive_1.is_for_water()
Explosive_2.is_for_water()
print("\n")


print("PARTE 2")
print("\n")


class BenchBlasting(Explosives):
    """
    Subclase que representa una tronadura de banco, heredando propiedades del explosivo base.

    Atributos adicionales:
    ----------------------
    drill_diameter_mm : float
        Diámetro del pozo de perforación en milímetros.
    burden_distance_m : float
        Distancia entre filas de pozos (burden) en metros.
    spacing_distance_m : float
        Distancia entre pozos en la misma fila en metros.
    bench_height_m : float
        Altura del banco en metros.
    subdrill_length_m : float
        Longitud adicional de perforación (pasadura) en metros.
    stemming_length_m : float
        Longitud del taco o tapón en collar en metros.
    explosive_unit_cost : float
        Costo del explosivo por kilogramo.
    drilling_unit_cost : float
        Costo por metro de perforación.

    Métodos:
    --------
    get_charge_factor():
        Calcula el factor de carga del explosivo (kg/m³).

    get_anfo_equivalent():
        Calcula el factor de carga equivalente en ANFO.

    get_blasting_cost():
        Calcula el costo total de la tronadura por metro cúbico ($/m³).
    """

    def __init__(self, commercial_name, explosive_density, vod, rws, water_resistance,
                 drill_diameter_mm, burden_distance_m, spacing_distance_m, bench_height_m,
                 subdrill_length_m, stemming_length_m, explosive_unit_cost, drilling_unit_cost):

        super().__init__(commercial_name, explosive_density * 1000, vod, rws, water_resistance)

        self.drill_diameter_mm = drill_diameter_mm
        self.burden_distance_m = burden_distance_m
        self.spacing_distance_m = spacing_distance_m
        self.bench_height_m = bench_height_m
        self.subdrill_length_m = subdrill_length_m
        self.stemming_length_m = stemming_length_m
        self.explosive_unit_cost = explosive_unit_cost
        self.drilling_unit_cost = drilling_unit_cost

    def get_charge_factor(self):
        drill_diameter_m = self.drill_diameter_mm / 1000
        charge_length = self.bench_height_m + \
            self.subdrill_length_m - self.stemming_length_m
        volume_per_blast = self.burden_distance_m * \
            self.spacing_distance_m * self.bench_height_m
        explosive_mass = (3.1416 / 4) * drill_diameter_m**2 * \
            charge_length * self.explosive_density
        return explosive_mass / volume_per_blast

    def get_anfo_equivalent(self):
        return self.get_charge_factor() * self.rws

    def get_blasting_cost(self):
        total_drill_depth = self.bench_height_m + self.subdrill_length_m
        cost_drilling = total_drill_depth * self.drilling_unit_cost

        drill_diameter_m = self.drill_diameter_mm / 1000
        charge_length = self.bench_height_m + \
            self.subdrill_length_m - self.stemming_length_m
        explosive_mass = (3.1416 / 4) * drill_diameter_m**2 * \
            charge_length * self.explosive_density
        cost_explosive = explosive_mass * self.explosive_unit_cost

        total_cost = cost_drilling + cost_explosive
        volume_per_blast = self.burden_distance_m * \
            self.spacing_distance_m * self.bench_height_m

        return total_cost / volume_per_blast


# Instancia de tronadura usando el explosivo Tronex Plus con parámetros geométricos y del explosivo.
tronadura_tronex = BenchBlasting(
    commercial_name='Tronex Plus',
    explosive_density=1.18,      # g/cm³
    vod=5200,                    # m/s
    rws=1.22,                    # Relación de potencia con ANFO
    water_resistance='Si',
    drill_diameter_mm=140,       # mm
    burden_distance_m=3.5,       # m
    spacing_distance_m=4.0,      # m
    bench_height_m=10,           # m
    subdrill_length_m=0.5,       # m
    stemming_length_m=2.0,       # m
    explosive_unit_cost=3.5,     # $/kg
    drilling_unit_cost=15.0      # $/m
)

# a) Calcular el factor de carga para el explosivo seleccionado:

print(
    f"El factor de carga para el explosivo seleccionado es {tronadura_tronex.get_charge_factor():.2f} kg/m³")
print("\n")

# b) Calcular el factor de carga pero equivalente a ANFO:

print(
    f"El factor de carga equivalente a ANFO es {tronadura_tronex.get_anfo_equivalent():.2f} kg/m³")
print("\n")

# c) Calcular el costo de la tronadura:

print(
    f"El costo de la tronadura segun los parámetros geométricos y del explosivo es {tronadura_tronex.get_blasting_cost():.2f} $/m³")
print("\n")
