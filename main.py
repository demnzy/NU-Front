import flet as ft
from src.Login import login_view
from src.signup import Signup_view

def main(page: ft.Page):
    page.banner = None 
    
    page.views.clear()
    page.title = "Nu-age"
    page.window_width = 400
    page.window_height = 650
    page.theme = ft.Theme(
    page_transitions=ft.PageTransitionsTheme(
        windows="fadeUpwards",  # Use lowercase strings
        android="fadeUpwards",
        ios="cupertino",
        macos="zoom"
    )
)

    def route_change(e):
        page.views.clear()

        if page.route == "/":
            page.views.append(login_view(page))
        elif page.route == "/signup":
            page.views.append(Signup_view(page))
        

        page.update()

    page.on_route_change = route_change

    route_change(None)

ft.run(main)