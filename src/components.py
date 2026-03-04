import flet as ft

class SuccessPopup(ft.Stack):
    def __init__(self, on_close_callback):
        super().__init__()
        self.on_close_callback = on_close_callback
        self.visible = False # Start hidden
        self.width = 300
        
        # 1. The Main White Card
        self.card = ft.Container(
            bgcolor=ft.Colors.WHITE,
            padding=ft.padding.only(top=40, left=20, right=20, bottom=20),
            border_radius=15,
            content=ft.Column(
                [
                    ft.Text("Submetido", size=20, weight="bold", color="black"),
                    ft.Text(
                        "Seus dados foram submetidos com sucesso!",
                        size=14, color="black54", text_align="center"
                    ),
                    ft.Container(height=10),
                    ft.ElevatedButton(
                        "OK", 
                        bgcolor="#009787", 
                        color="white",
                        width=120,
                        on_click=self.close_popup
                    )
                ],
                horizontal_alignment="center",
                spacing=10,
            )
        )

        # 2. The Floating Check Icon (Green Circle)
        self.icon_circle = ft.Container(
            content=ft.Icon(ft.Icons.CHECK, color="white", size=30),
            bgcolor="green",
            width=60,
            height=60,
            border_radius=30,
            top=-30, # Position it halfway above the card
            left=120, # Center it horizontally (300/2 - 60/2)
        )

        self.controls = [
            ft.Container(height=30), # Spacer for the top icon
            self.card,
            self.icon_circle
        ]

    def close_popup(self, e):
        self.visible = False
        self.update()
        if self.on_close_callback:
            self.on_close_callback()