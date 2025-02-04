import flet as ft

class ToDo:
    def __init__(self, page:ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width = 350
        self.page.window_height = 450
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = "Tarefas do dia"
        self.main_page()

    def main_page(self):
        input_task = ft.TextField(hint_text = "Digite uma tarefa")

        input_bar = ft.Row(
            controls={
                input_task,
                ft.FloatingActionButton(icon=ft.icons.ADD)
            }
        )

ft.app(target = ToDo)