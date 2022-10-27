# str = '0123456789'
#
# par = str[::2]
# print(f'Par={par}')
# impar = str[1::2]
# print(f'Par={impar}')

# pasaport = input("Detineti pasaport?")# confirmam cu da sau nu daca detinem pasaport
# if pasaport == "nu":#daca nu avem pasaport nu neputem imbarca si se opreste codul
#     print("Nu aveti permisiunea de imbarcare!")
# elif pasaport =="da":# daca avem pasaport ne va cere sa introducem varsta
#     varsta = int(input("Introduceti varsta:"))
#     if varsta >= 18:# daca avem 18 sau peste 18 ani ne putem imbarca
#         print(f"Persoana are varsta de {varsta} ani si detine pasaport!\n Va puteti imbarca!")
#     else:# daca avem sub 18 ani
#         if varsta < 18:
#             cu_mama = input("Calatoriti cu mama?")
#             cu_tata = input("Calatoriti cu tata?")
#         if cu_mama == 'da' and cu_tata == 'da':# si calatorim cu ambii parinti vom primi accept pentru imbarcare
#             print(f"Persoana are varsta sub {varsta} ani,detine pasaport si este insotita de ambii parinti!\n Va puteti imbarca!")
#         else:# altfel pentru a calatori doar cu un parinte ne trebuie permisiunea scrisa de la celalalt parinte
#             act_permisiune = input("Aveti permisiunea celuilalt parinte")
#             if cu_mama == 'da' or cu_tata == 'da' and act_permisiune=="da":# daca avem permisiunea de la un parinte si calatorim cu celalalt parinte
#                 # vom primi accept pentru imbarcare
#                 print(f"Persoana are varsta sub {varsta} ani,detine pasaport, este insotita de cel putin un parinte si are permisiunea de la celalalt parinte!\n Va puteti imbarca!")
#             else:
#                 print("Nu aveti permisiunea de imbarcare! ")#altfel nu vom primi accept pentru imbarcare


# class Todolist:
# #     to_do = {None: None}
# #
# #     def add_task(self):
# #         to_do_list.to_do = {"make_clean": "you have to vacuum, wipe the dust, air the room"}
# #         to_do_list.to_do.update({"make_shower": "Go to bathroom and wash your body"})
# #
# #     def end_task(self):
# #         to_do_list.to_do.pop("make_shower")
# #
# #     def print_to_do(self):
# #         for x in to_do_list.to_do:
# #             print(f'You have to do : {x}.')
# #
# #     def details_to_do(self):
# #         for y in to_do_list.to_do:
# #             print(f'These are the details for what you have to do : {to_do_list.to_do[y]}.')
# #         if "make_shower" not in to_do_list.to_do:
# #             answear = input(f'Do you want to add the task ?\n')
# #             if answear == 'yes':
# #                 details = (input(f'Please describe with details this task : \n'))
# #                 details2 = (input(f'Please describe with details this task : \n'))
# #                 to_do_list.to_do.fromkeys(details, details2)
# #                 return to_do_list.to_do
# #             elif answear == 'no':
# #                 print(f'Goodbye')
# #         else:
# #             print(f'This task exists .')
# #
# #
# # to_do_list = Todolist()
# # to_do_list.add_task()
# # to_do_list.end_task()
# # to_do_list.print_to_do()
# # print(to_do_list.details_to_do())


# class Todo:
#     todo = {None: None}
#     nume = None
#     descriere = None
#
#     def adauga_task(self):
#         x = input('Vrei sa adaugi task? \n')
#         if x == 'yes':
#             detalii1 = input('introdu nume task')
#             detalii2 = input('introdu descriere task')
#             self.todo.update({detalii1: detalii2})
#             return self.todo.items()
#         else:
#             print('la revedere')
#
#     def finalizare_task(self, nume):
#         x = input('introdu nume')
#         self.nume = x
#         print(nume)
#         if nume in self.todo.items():
#             self.todo.pop(self.nume, self.descriere)
#             print(self.todo)
#         else:
#             print('nu gasim task-ul')
#
#     def detalii(self):
#         if self.todo.keys:
#             print('exista task-ul')
#         else:
#             print('Nu exista task-ul')
#
#
# task = Todo()
# print(task.adauga_task())
# task.finalizare_task('test')
