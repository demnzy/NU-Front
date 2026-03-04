import flet as ft

def Signup_view(page: ft.Page):
    Signup_form= ft.Container(
        width=400,
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border_radius=15,
        height=560,
        content=ft.Column(controls=[
        ft.Text("Signup for Nu-age", size=30, weight=ft.FontWeight.BOLD),
        ft.Row(controls=[ft.Text("Please enter your details to create an account.", size=14, color="#009787")]),
        ft.Divider(),
        ft.Row(controls=[ft.TextField(label="First Name", width=175, height=35, text_size=13),ft.TextField(label="Last Name", width=175, height=35, text_size=13)]),
        ft.Row(controls=[ft.TextField(label="Email", width=360, height=35, text_size=13)]),
        ft.Row(controls=[ft.TextField(label="Username", width=360, height=35, text_size=13)]),
        ft.Row(controls=[ft.TextField(label="Password", password=True, can_reveal_password=True, width=360, height=35, text_size=13)]),
        ft.Row(controls=[ft.TextField(label="Confirm Password", password=True, can_reveal_password= True, width=  360, height=35, text_size=13)]),
        ft.Checkbox(label="I accept the Terms of use & Privacy Policy", value=True),
        ft.Button("Sign Up", width=350, color=ft.Colors.BLACK, bgcolor="#009787", height=40)],
                          spacing=20,))
    
    return ft.View(
        route="/signup",
        controls=[Signup_form],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor="#009787",
    )