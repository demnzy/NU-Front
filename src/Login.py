import flet as ft
from src.requests.auth import login_request
def login_view(page: ft.Page):
    is_processing = False
    custom_message=ft.Text("", size=14)
    
    def handle_action_click(e: ft.Event[ft.CupertinoDialogAction]):
        page.pop_dialog()

    cupertino_alert_dialog = ft.CupertinoAlertDialog(
        title=ft.Row(controls=[ft.Text("Login Successful!", size =20),ft.Icon(ft.Icons.CHECK, color="#009787")]),
        actions=[
            ft.CupertinoDialogAction(
                content=ft.Text("Ok", color="#009787"),
                destructive=True,
                on_click=handle_action_click,
            ),
        ],
    )
    
    User_Not_found = ft.CupertinoAlertDialog(
        title=ft.Row(controls=[ft.Text("Login Failed!", size =20), ft.Icon(ft.Icons.CLOSE, color="#009787")]),
        content=custom_message,
        actions=[
            ft.CupertinoDialogAction(
                content=ft.Text("Ok", color="#009787"),
                destructive=True,
                on_click=handle_action_click,
            ),
        ],
    )



    def validate_inputs(e):
        password_value = password.value.strip()
        email_value = email.value.strip()
        
        
        if not (email_value and password_value):
            Submit.disabled = True
            page.update()
        else:
            Submit.disabled = False
            page.update()
    
    async def handle_submit(e):
        nonlocal is_processing
        Submit.disabled = True
        page.update()
        if is_processing:
            return
            
        is_processing = True
        Submit.disabled = True
        Submit.content = "Authenticating..." # Visual feedback
        page.update()
        try:
            status,data = await login_request(email.value, password.value)   
            if status == 200:
                Submit.bgcolor = "#009787" 
                page.show_dialog(cupertino_alert_dialog)
            elif status == 404:
                custom_message.value="This account does not exist. Please check your email and try again."
                page.update()
                page.show_dialog(User_Not_found)
                Submit.disabled = False
                page.update()

            elif status == 403:
                Submit.bgcolor = "#009787" 
                page.update()
                custom_message.value="Incorrect Password. Please try again"
                page.show_dialog(User_Not_found)
                Submit.disabled = False
                page.update()
        finally:
            is_processing = False
            Submit.content = "Login"
            page.update()
            
    email= ft.TextField(label="Email/Username", width=270, height=35, text_size=13, on_change=validate_inputs)
    password = ft.TextField(label="Password", password=True, can_reveal_password= True, width=270, height=35, text_size=13, on_change=validate_inputs)
    Submit = ft.Button("Login", width=320, color=ft.Colors.BLACK, bgcolor="#009787", height=40,disabled=True, on_click=handle_submit)
    
    login_card = ft.Container(
        width=350,
        padding=20,
        bgcolor=ft.Colors.WHITE,
        border_radius=15,
        height=530,
        
        shadow=ft.BoxShadow(
            blur_radius=15,
            color=ft.Colors.with_opacity(0.2, "black"),
            offset=ft.Offset(0, 5)
        ),

        content=ft.Column(
            [
                ft.Icon(ft.Icons.ACCOUNT_CIRCLE, 
                color="#009787", 
                size=100
            ),
                ft.Text("Welcome Back!", size=24, weight=ft.FontWeight.BOLD),
                ft.Row(controls=[
                    ft.Icon(ft.Icons.MAIL_OUTLINE, 
                color="#009787", 
                width=20,
                height=40
            ),
                email]),
                ft.Row(controls=[
                    ft.Icon(ft.Icons.VPN_KEY, 
                color="#009787", 
                width=20,
                height=40
            ),
                password]),
                ft.Row(controls=[ft.Container(width=37),
                    ft.Column(controls=[
                        ft.TextButton(content="Forgot Password"),
                        
                    ],horizontal_alignment=ft.CrossAxisAlignment.START),
                    ft.Column(controls=[
                        ft.TextButton(content="Sign Up", on_click=lambda _: page.go("/signup")),
                        
                    ],horizontal_alignment=ft.CrossAxisAlignment.END)]),
                ft.Container(expand=True),
                Submit
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=35
        )
    )

    return ft.View(
        route="/",
        controls=[login_card],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        bgcolor="#009787",
    )