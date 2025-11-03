import flet as ft

def main(page: ft.Page):
    # إعدادات الصفحة
    page.title = "تطبيق Flet بسيط"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # متغيرات التطبيق
    counter = 0
    
    def increment_counter(e):
        nonlocal counter
        counter += 1
        counter_text.value = f"العداد: {counter}"
        page.update()
    
    def reset_counter(e):
        nonlocal counter
        counter = 0
        counter_text.value = f"العداد: {counter}"
        page.update()
    
    def change_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT 
            else ft.ThemeMode.LIGHT
        )
        theme_button.text = (
            "تفعيل الوضع النهاري" if page.theme_mode == ft.ThemeMode.DARK 
            else "تفعيل الوضع الليلي"
        )
        page.update()
    
    # عناصر الواجهة
    title = ft.Text(
        "مرحباً بك في تطبيق Flet!",
        size=24,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )
    
    counter_text = ft.Text(
        f"العداد: {counter}",
        size=20,
        text_align=ft.TextAlign.CENTER
    )
    
    increment_button = ft.ElevatedButton(
        "زيادة العداد",
        on_click=increment_counter,
        icon=ft.icons.ADD
    )
    
    reset_button = ft.ElevatedButton(
        "إعادة تعيين",
        on_click=reset_counter,
        icon=ft.icons.REFRESH
    )
    
    theme_button = ft.ElevatedButton(
        "تفعيل الوضع الليلي",
        on_click=change_theme,
        icon=ft.icons.DARK_MODE
    )
    
    # إضافة العناصر إلى الصفحة
    page.add(
        ft.Column(
            [
                title,
                ft.Divider(),
                counter_text,
                ft.Row(
                    [increment_button, reset_button],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                theme_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

# تشغيل التطبيق
if __name__ == "__main__":
    ft.app(target=main)
