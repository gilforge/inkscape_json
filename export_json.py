#!/usr/bin/env python
# coding=utf-8
#
# Copyright (C) 2023 Giforge, gilles.forge@gmail.com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

"""
Exporte les coordonnées des tracés d'un fichier Inkscape dans un fichier JSON à choisir par l'utilisateur
"""
# import inkex
# import json
# from tkinter import Tk
# from tkinter.filedialog import asksaveasfilename

# class ExportPathsToJson(inkex.EffectExtension):
#     def effect(self):
#         # Récupérer les éléments sélectionnés
#         selected_elements = self.svg.selected

#         # Préparer le dictionnaire qui sera converti en JSON
#         json_dict = {}

#         # Parcourir les éléments sélectionnés
#         for id, element in selected_elements.items():
#             # Vérifier si l'élément est un tracé
#             if isinstance(element, inkex.PathElement):
#                 # Récupérer les coordonnées du tracé
#                 path_data = element.path.to_superpath()

#                 # Ajouter les coordonnées au dictionnaire
#                 json_dict[id] = path_data

#         # Convertir le dictionnaire en JSON
#         json_output = json.dumps(json_dict)

#         # Ouvrir une boîte de dialogue pour choisir le fichier de sauvegarde
#         Tk().withdraw() # Cacher la fenêtre Tkinter
#         file_path = asksaveasfilename(defaultextension=".json")

#         # Écrire le JSON dans un fichier
#         with open(file_path, 'w') as json_file:
#             json_file.write(json_output)

# if __name__ == '__main__':
#     ExportPathsToJson().run()

"""
Même code, avec l'arrondi des coordonnées dans le fichier de sortie
"""
import inkex
import json
from tkinter import Tk
from tkinter.filedialog import asksaveasfilename

class ExportPathsToJson(inkex.EffectExtension):
    def effect(self):
        # Récupérer les éléments sélectionnés
        selected_elements = self.svg.selected

        # Préparer la liste qui sera convertie en JSON
        json_list = []

        # Parcourir les éléments sélectionnés
        for id, element in selected_elements.items():
            # Vérifier si l'élément est un tracé
            if isinstance(element, inkex.PathElement):
                # Récupérer les coordonnées du tracé
                path_data = element.path.to_superpath()

                # Parcourir chaque sous-tracé
                for subpath in path_data:
                    # Ajouter le point de départ et le point d'arrivée à la liste
                    start_point = subpath[0][1]
                    end_point = subpath[-1][1]
                    # json_list.append([start_point[0], start_point[1], end_point[0], end_point[1]])
                    json_list.append([round(start_point[0]), round(start_point[1]), round(end_point[0]), round(end_point[1])])

        # Convertir la liste en JSON
        json_output = json.dumps(json_list)

        # Ouvrir une boîte de dialogue pour choisir le fichier de sauvegarde
        Tk().withdraw() # Cacher la fenêtre Tkinter
        file_path = asksaveasfilename(defaultextension=".json")

        # Écrire le JSON dans un fichier
        with open(file_path, 'w') as json_file:
            json_file.write(json_output)

if __name__ == '__main__':
    ExportPathsToJson().run()
