from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.core.window import Window

class AnimatedWelcomeApp(App):
    def build(self):
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        
        layout = BoxLayout(orientation='vertical', padding=50, spacing=30)
        
        # الزر مع تأثيرات
        self.button = Button(
            text='🎉 اضغط هنا 🎉',
            size_hint=(0.6, 0.4),
            pos_hint={'center_x': 0.5},
            font_size='22sp',
            background_color=(0.3, 0.7, 0.3, 1),
            color=(1, 1, 1, 1)
        )
        self.button.bind(on_press=self.animate_welcome)
        
        # التسمية
        self.label = Label(
            text='',
            font_size='28sp',
            color=(0.8, 0.2, 0.2, 1),
            bold=True
        )
        
        layout.add_widget(self.button)
        layout.add_widget(self.label)
        
        return layout
    
    def animate_welcome(self, instance):
        # تأثير اهتزاز للزر
        anim = Animation(center_x=300, duration=0.1) + Animation(center_x=250, duration=0.1)
        anim.start(instance)
        
        # عرض رسالة الترحيب
        self.label.text = "🎊 نرحب بكم 🎊"
        
        # تأثير للتسمية
        anim_label = Animation(font_size=32, duration=0.3) + Animation(font_size=28, duration=0.3)
        anim_label.start(self.label)

if __name__ == '__main__':
    AnimatedWelcomeApp().run()
