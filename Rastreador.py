# url https://www.youtube.com/watch?v=dRVPONsESqw&t=450s
import math

# Creamos una clase para nuestro rastreador


class Rastreador:
    # inicializamos variables
    def __init__(self):
        # Almacecnamos posiciones centrales de los objetos
        self.centro_puntos = {}
        # contador de objetos
        self.id_count = 1

    def rastreo(self, objetos):
        # Almacenamiento de los objetos identificados
        objetos_id = []

        # Obtener punto central del nuevo objeto
        for rect in objetos:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            # Miramos si ese objeto ya fue detectado
            objeto_det = False
            for id, pt in self.centro_puntos.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])

                if dist < 25:
                    self.centro_puntos[id] = (cx, cy)
                    print(self.centro_puntos)
                    objetos_id.append([x, y, w, h, id])
                    objetos_det = True
                    break
            # Si es un nuevo objeto le asignamos un id
            if objeto_det is False:
                # Asignamos valor a las coordenadas X y Y
                self.centro_puntos[self.id_count] = (cx, cy)
                # agregamos al objeto su id
                objetos_id.append([x, y, w, h, self.id_count])
                self.id_count = self.id_count + 1  # Aumentamos el ID

        # Limpiar la lista de por puntos centrales para eliminar IDS que ya no se usan
        new_center_points = {}
        for obj_bb_id in objetos_id:
            _, _, _, _, object_id = obj_bb_id
            center = self.centro_puntos[object_id]
            new_center_points[object_id] = center

        # Actualizar la lista con ID NO utilizados o eliminados
        self.centro_puntos = new_center_points.copy()
        return objetos_id
