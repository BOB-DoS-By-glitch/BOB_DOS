from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.progressbar import ProgressBar
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import os
import base64
import zipfile
import shutil
import tempfile
import subprocess
import uuid
import datetime
import sys

# Set window size
Window.size = (800, 900)
Window.clearcolor = get_color_from_hex('#121212')

def install():
    try:
        import cython
        print('# - Cython is already installed')
    except ImportError:
        print('# - Installing cython...')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'cython'])
        import cython

def xor_base64_enc(data: str, key: list) -> str:
    return ''.join([chr(ord(c) ^ key[i % len(key)]) for i, c in enumerate(data)])

def enc_line(lines, keys):
    lll = []
    for line in lines:
        line = line.rstrip('\n')
        s1 = xor_base64_enc(line, keys['key1'])
        s2 = xor_base64_enc(s1, keys['key2'])
        b64_encoded = base64.b64encode(s2.encode()).decode()
        lll.append(b64_encoded)
    return lll

def enc(lll, keys, user_id, user_token):
    return f'''
import base64

def ll(data: str, key: list) -> str:
    return ''.join([chr(ord(c) ^ key[i % len(key)]) for i, c in enumerate(data)])

def run(lll, keys):
    l = []
    for enc in lll:
        s = base64.b64decode(enc).decode()
        s = ll(s, keys["key2"])
        s = ll(s, keys["key1"])
        l.append(s)
    return "\\n".join(l)

# User credentials
ID = "{user_id}"
Token = "{user_token}"

lll = {repr(lll)}
keys = {{"key1": {keys["key1"]},"key2": {keys["key2"]}}}

code = run(lll, keys)
exec(code)
'''

def add_expiry_check(code, expiry_date, username):
    expiry_code = f"""
import os
import datetime
now = datetime.date.today()
target = datetime.date({expiry_date.year}, {expiry_date.month}, {expiry_date.day})
if now >= target:
    exit(f" - Turn Off This Tool ... ! Please Wait For {username}")
"""
    return expiry_code + "\n" + code

def add_server_check(code, server_url):
    server_code = f"""
Server = None
try:
    Check_Server = __import__('requests').get('{server_url}').text
    if 'ON' in Check_Server:
        Server = True
        print("✓ Server Status: Active")
    else:
        print("✗ Server Status: Offline")
        print(f'- Turn Off This Tool ... ! Please Wait For -')
        exit()
except:
    print("✗ Server Status: Connection Failed")
    print(f'- Turn Off This Tool ... ! Please Wait For -')
    exit()
"""
    return server_code + "\n" + code

def elf(source_path, working_dir, protection_type, user_id, user_token, expiry_date=None, username=None, server_url=None):
    install()
    keys = {
        'key1': [57, 86, 161, 120, 219, 27, 229, 199, 203, 14, 186, 181, 233, 27, 149, 196, 69, 19, 179, 3, 74, 180, 28, 108, 120, 218, 130, 20, 162, 9, 28, 239, 229, 177, 215],
        'key2': [89, 112, 199, 20, 188, 180, 138, 41, 94, 79, 150, 166, 144, 246, 180, 42, 219, 68, 26, 40, 38, 192, 98, 98, 145, 219, 199, 162, 183, 97, 104, 101, 197, 164, 59, 251, 64, 108, 103, 139]
    }

    with open(source_path, 'r', encoding='utf-8', errors='ignore') as f:
        original_code = f.read()
    
    # Add protection based on selected type
    if protection_type == 'expiry':
        if not expiry_date or not username:
            raise Exception("Expiry date and username are required for expiry protection")
        modified_code = add_expiry_check(original_code, expiry_date, username)
    elif protection_type == 'server':
        if not server_url:
            raise Exception("Server URL is required for server protection")
        modified_code = add_server_check(original_code, server_url)
    else:
        modified_code = original_code
    
    # Write modified code to temporary file
    modified_path = os.path.join(working_dir, 'modified_input.py')
    with open(modified_path, 'w', encoding='utf-8') as f:
        f.write(modified_code)
    
    # Process the modified file
    with open(modified_path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    lll = enc_line(lines, keys)
    final_code = enc(lll, keys, user_id, user_token)
    
    r = """
# - Enc : Plya_Team - BY - LAEGER_MO OR @sis_c   
__J=''
__C=chr
import zipfile as I,os as o,shutil as K,tempfile as T,sys as s,platform as M,subprocess as P
def NinjramPro():
 A=o.path.dirname(o.path.abspath(s.argv[0]));B=T.mkdtemp();
 try:
  C=o.path.abspath(s.argv[0]);
  with I.ZipFile(C,(__J.join(__C(c^106) for c in [24])))as D:D.extractall(B);
  E=M.machine();F={(__J.join(__C(c^16) for c in [81, 93, 84, 38, 36])):(__J.join(__C(c^242) for c in [188, 155, 156, 152, 128, 147, 159, 162, 128, 157, 196, 198])),(__J.join(__C(c^161) for c in [217, 153, 151, 254, 151, 149])):(__J.join(__C(c^189) for c in [243, 212, 211, 215, 207, 220, 208, 237, 207, 210, 139, 137])),(__J.join(__C(c^207) for c in [174, 174, 189, 172, 167, 249, 251])):(__J.join(__C(c^12) for c in [66, 101, 98, 102, 126, 109, 97, 92, 126, 99, 58, 56])),(__J.join(__C(c^207) for c in [174, 189, 162, 185, 248, 163])):(__J.join(__C(c^114) for c in [60, 27, 28, 24, 0, 19, 31, 34, 0, 29, 65, 64])),(__J.join(__C(c^86) for c in [55, 36, 59, 32, 110, 58])):(__J.join(__C(c^124) for c in [50, 21, 18, 22, 14, 29, 17, 44, 14, 19, 79, 78])),(__J.join(__C(c^10) for c in [107, 120, 103, 60, 62])):(__J.join(__C(c^12) for c in [66, 101, 98, 102, 126, 109, 97, 92, 126, 99, 58, 56])),(__J.join(__C(c^186) for c in [194, 130, 140])):(__J.join(__C(c^30) for c in [80, 119, 112, 116, 108, 127, 115, 78, 108, 113, 45, 44])),(__J.join(__C(c^29) for c in [116, 46, 37, 43])):(__J.join(__C(c^92) for c in [18, 53, 50, 54, 46, 61, 49, 12, 46, 51, 111, 110])),(__J.join(__C(c^207) for c in [166, 249, 247, 249])):(__J.join(__C(c^209) for c in [159, 184, 191, 187, 163, 176, 188, 129, 163, 190, 226, 227]))};
  if E not in F:print(f"Unsupported machine architecture: {E}");s.exit(1);
  G=F[E];H=o.path.join(B,G);
  if not o.path.exists(H):print(f"Binary not found for architecture: {E} at path: {H}");s.exit(1);
  o.chmod(H,0o755);o.chdir(A);P.run([H]+s.argv[1:]);
 except I.BadZipFile:print((__J.join(__C(c^130) for c in [199, 240, 240, 237, 240, 184, 162, 214, 234, 235, 241, 162, 231, 250, 231, 225, 247, 246, 227, 224, 238, 231, 162, 235, 241, 162, 236, 237, 246, 162, 227, 162, 244, 227, 238, 235, 230, 162, 216, 203, 210, 162, 228, 235, 238, 231, 162, 237, 240, 162, 235, 241, 162, 225, 237, 240, 240, 247, 242, 246, 231, 230, 172])));
 except Exception as J:print(f"An error occurred: {J}");
 finally:
  try:K.rmtree(B);
  except Exception as L:print(f"Warning: Could not remove temporary directory: {L}");

if __name__==(__J.join(__C(c^60) for c in [99, 99, 81, 93, 85, 82, 99, 99])):NinjramPro();
    """

    o_py_path = os.path.join(working_dir, "oo.py")
    c_path = os.path.join(working_dir, "NinjcythonPro.c")
    main_py_path = os.path.join(working_dir, '__main__.py')
    bin32 = os.path.join(working_dir, "NinjramPro32")
    bin64 = os.path.join(working_dir, "NinjramPro64")

    with open(o_py_path, "w", encoding='utf-8') as f:
        f.write(final_code)

    try:
        subprocess.run(['cython', '--embed', '-3', '--directive', 'annotation_typing=False', '-o', c_path, o_py_path], check=True)
        subprocess.run(['gcc', '-w', '-m32', c_path, '-o', bin32, '-fvisibility=hidden', '-s', '-fno-stack-protector', 
                      '-fPIE', '-pie', '-fomit-frame-pointer', '-Wl,-z,relro,-z,now', '-Wl,-s'] + 
                      subprocess.check_output(['python3-config', '--cflags', '--ldflags']).decode().split(), check=True)
    except subprocess.CalledProcessError as e:
        raise Exception(f"Compilation failed: {e}")

    with open(main_py_path, 'w', encoding='utf-8') as run_elf:
        run_elf.write(r)

    zip_file = os.path.join(working_dir, '.NinjiGramPro')
    with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(main_py_path, arcname='__main__.py')
        zipf.write(bin32, arcname='NinjramPro32')

    with open(zip_file,'rb') as file_base64:
        read_file = file_base64.read()
    base64_src = base64.b64encode(read_file).decode()

    NinjiGramPro = f'''
import os, sys, base64 as B
A = '.NinjiGramPro'
C = {base64_src!r}
try:
    with open(A,'wb')as D:D.write(B.b64decode(C))
    os.system('python3 .NinjiGramPro '+' '.join(sys.argv[1:]))
except Exception as E:print(E)
finally:
    if os.path.exists(A):os.remove(A)
'''

    # Save to /sdcard/ENC_Plya_Team
    storage_path = "/sdcard/ENC_Plya_Team"
    os.makedirs(storage_path, exist_ok=True)
    final_output = os.path.join(storage_path, 'Enc_NinjiGramPro.py')
    
    with open(final_output, 'w') as n:
        n.write(NinjiGramPro)

    return final_output

class StyledButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = get_color_from_hex('#00cc99')
        self.color = get_color_from_hex('#ffffff')
        self.size_hint_y = None
        self.height = 50
        self.font_size = 16

class StyledTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = get_color_from_hex('#1e1e1e')
        self.foreground_color = get_color_from_hex('#eeeeee')
        self.size_hint_y = None
        self.height = 40
        self.multiline = False
        self.padding = [10, 10]

class StyledLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = get_color_from_hex('#eeeeee')
        self.size_hint_y = None
        self.height = 30

class HeaderLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.color = get_color_from_hex('#00ffcc')
        self.font_size = 18
        self.bold = True
        self.size_hint_y = None
        self.height = 40

class ProtectionToggle(ToggleButton):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = get_color_from_hex('#1e1e1e')
        self.color = get_color_from_hex('#eeeeee')
        self.size_hint_y = None
        self.height = 40
        self.group = 'protection'

class FileChooserPopup(Popup):
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Select Python File'
        self.size_hint = (0.9, 0.8)
        self.callback = callback
        
        layout = BoxLayout(orientation='vertical')
        
        filechooser = FileChooserListView(filters=['*.py'])
        layout.add_widget(filechooser)
        
        btn_layout = BoxLayout(size_hint_y=None, height=50)
        btn_select = Button(text='Select', background_color=get_color_from_hex('#00cc99'))
        btn_cancel = Button(text='Cancel', background_color=get_color_from_hex('#cc0000'))
        
        btn_select.bind(on_press=lambda x: self.select_file(filechooser))
        btn_cancel.bind(on_press=self.dismiss)
        
        btn_layout.add_widget(btn_select)
        btn_layout.add_widget(btn_cancel)
        layout.add_widget(btn_layout)
        
        self.content = layout
    
    def select_file(self, filechooser):
        if filechooser.selection:
            self.callback(filechooser.selection[0])
            self.dismiss()

class NinjiGramProApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected_file = None
        self.protection_type = "expiry"
        self.time_label = None

    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = self.create_header()
        main_layout.add_widget(header)
        
        # Scrollable content
        scroll = ScrollView()
        content = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))
        
        # Add content widgets
        content.add_widget(self.create_file_section())
        content.add_widget(self.create_credentials_section())
        content.add_widget(self.create_protection_section())
        content.add_widget(self.create_action_section())
        content.add_widget(self.create_info_section())
        
        scroll.add_widget(content)
        main_layout.add_widget(scroll)
        
        # Start clock updates
        Clock.schedule_interval(self.update_time, 1)
        
        return main_layout
    
    def create_header(self):
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=60)
        
        # Time display
        time_layout = BoxLayout(orientation='horizontal', size_hint_x=0.3)
        self.time_label = Label(text='00:00:00', color=get_color_from_hex('#00ffcc'), font_size=16)
        time_status = Label(text='✓', color=get_color_from_hex('#000000'), 
                          font_size=14, bold=True)
        time_status.background_color = get_color_from_hex('#00ff00')
        
        time_layout.add_widget(self.time_label)
        time_layout.add_widget(time_status)
        
        # Title
        title = Label(text='NinjiGramPro', font_size=24, bold=True,
                     color=get_color_from_hex('#ff0000'))
        
        # Profile button
        profile_btn = Button(text='ⓘ', font_size=20, size_hint_x=0.1,
                           background_color=get_color_from_hex('#00ffcc'))
        profile_btn.bind(on_press=self.show_info_popup)
        
        header.add_widget(time_layout)
        header.add_widget(title)
        header.add_widget(profile_btn)
        
        return header
    
    def create_file_section(self):
        section = BoxLayout(orientation='vertical', size_hint_y=None, height=120)
        
        title = HeaderLabel(text='File Selection')
        section.add_widget(title)
        
        self.file_btn = StyledButton(text='Choose Python File')
        self.file_btn.bind(on_press=self.show_file_chooser)
        section.add_widget(self.file_btn)
        
        self.file_label = StyledLabel(text='No file selected')
        section.add_widget(self.file_label)
        
        return section
    
    def create_credentials_section(self):
        section = BoxLayout(orientation='vertical', size_hint_y=None, height=120)
        
        title = HeaderLabel(text='Credentials')
        section.add_widget(title)
        
        self.user_id_input = StyledTextInput(hint_text='Enter your ID')
        section.add_widget(self.user_id_input)
        
        self.user_token_input = StyledTextInput(hint_text='Enter your token')
        section.add_widget(self.user_token_input)
        
        return section
    
    def create_protection_section(self):
        section = BoxLayout(orientation='vertical', size_hint_y=None, height=300)
        
        title = HeaderLabel(text='Protection Type')
        section.add_widget(title)
        
        # Protection toggle buttons
        toggle_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)
        
        self.expiry_toggle = ProtectionToggle(text='Expiry Date Protection')
        self.server_toggle = ProtectionToggle(text='Server Check Protection')
        
        self.expiry_toggle.state = 'down'
        
        self.expiry_toggle.bind(on_press=self.on_protection_changed)
        self.server_toggle.bind(on_press=self.on_protection_changed)
        
        toggle_layout.add_widget(self.expiry_toggle)
        toggle_layout.add_widget(self.server_toggle)
        section.add_widget(toggle_layout)
        
        # Expiry section
        self.expiry_section = BoxLayout(orientation='vertical', size_hint_y=None, height=150)
        
        self.expiry_date_input = StyledTextInput(hint_text='YYYY-MM-DD')
        self.username_input = StyledTextInput(hint_text='@your_username')
        
        expiry_note = StyledLabel(text='Tool will stop working after this date', font_size=12)
        
        self.expiry_section.add_widget(StyledLabel(text='Expiry Date:'))
        self.expiry_section.add_widget(self.expiry_date_input)
        self.expiry_section.add_widget(StyledLabel(text='Your Username:'))
        self.expiry_section.add_widget(self.username_input)
        self.expiry_section.add_widget(expiry_note)
        
        # Server section
        self.server_section = BoxLayout(orientation='vertical', size_hint_y=None, height=100)
        self.server_section.visible = False
        
        self.server_url_input = StyledTextInput(hint_text='https://example.com/status.txt')
        server_note = StyledLabel(text='Tool will check this URL for ON status', font_size=12)
        
        self.server_section.add_widget(StyledLabel(text='Server URL:'))
        self.server_section.add_widget(self.server_url_input)
        self.server_section.add_widget(server_note)
        
        section.add_widget(self.expiry_section)
        section.add_widget(self.server_section)
        
        return section
    
    def create_action_section(self):
        section = BoxLayout(orientation='vertical', size_hint_y=None, height=100)
        
        self.encrypt_btn = StyledButton(text='Encrypt Files')
        self.encrypt_btn.bind(on_press=self.encrypt_file)
        self.encrypt_btn.disabled = True
        section.add_widget(self.encrypt_btn)
        
        self.status_label = StyledLabel(text='', color=get_color_from_hex('#00ff00'))
        self.error_label = StyledLabel(text='', color=get_color_from_hex('#ff0000'))
        
        section.add_widget(self.status_label)
        section.add_widget(self.error_label)
        
        return section
    
    def create_info_section(self):
        section = BoxLayout(orientation='vertical', size_hint_y=None, height=200)
        
        # How to use
        how_to_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=120)
        how_to_layout.background_color = get_color_from_hex('#1e1e1e')
        
        how_to_title = HeaderLabel(text='How to Use')
        how_to_layout.add_widget(how_to_title)
        
        steps = [
            "1. Click 'Choose Python File' to select your file",
            "2. Fill in your credentials",
            "3. Select protection type and configure",
            "4. Click 'Encrypt Files' to start encryption"
        ]
        
        for step in steps:
            how_to_layout.add_widget(StyledLabel(text=step, font_size=12))
        
        section.add_widget(how_to_layout)
        
        return section
    
    def update_time(self, dt):
        now = datetime.datetime.now()
        self.time_label.text = now.strftime("%H:%M:%S")
    
    def show_file_chooser(self, instance):
        popup = FileChooserPopup(self.on_file_selected)
        popup.open()
    
    def on_file_selected(self, file_path):
        self.selected_file = file_path
        self.file_label.text = f"Selected: {os.path.basename(file_path)}"
        self.encrypt_btn.disabled = False
    
    def on_protection_changed(self, instance):
        if instance.text == 'Expiry Date Protection':
            self.protection_type = "expiry"
            self.expiry_section.height = 150
            self.expiry_section.visible = True
            self.server_section.height = 0
            self.server_section.visible = False
        else:
            self.protection_type = "server"
            self.expiry_section.height = 0
            self.expiry_section.visible = False
            self.server_section.height = 100
            self.server_section.visible = True
        
        # Force layout update
        self.root.do_layout()
    
    def encrypt_file(self, instance):
        if not self.selected_file:
            self.error_label.text = "Please select a file first"
            return
        
        user_id = self.user_id_input.text
        user_token = self.user_token_input.text
        
        if not user_id or not user_token:
            self.error_label.text = "ID and Token are required"
            return
        
        try:
            if self.protection_type == "expiry":
                expiry_date_str = self.expiry_date_input.text
                username = self.username_input.text
                if not expiry_date_str or not username:
                    self.error_label.text = "Expiry date and username are required"
                    return
                expiry_date = datetime.datetime.strptime(expiry_date_str, '%Y-%m-%d').date()
                server_url = None
            else:
                server_url = self.server_url_input.text
                if not server_url:
                    self.error_label.text = "Server URL is required"
                    return
                expiry_date = None
                username = None
            
            # Show loading state
            self.encrypt_btn.text = "Encrypting..."
            self.encrypt_btn.disabled = True
            self.status_label.text = "Starting encryption process..."
            
            # Process in a separate thread to avoid UI freeze
            Clock.schedule_once(lambda dt: self._do_encryption(user_id, user_token, expiry_date, username, server_url), 0.1)
            
        except Exception as e:
            self.error_label.text = f"Error: {str(e)}"
            self.encrypt_btn.text = "Encrypt Files"
            self.encrypt_btn.disabled = False
    
    def _do_encryption(self, user_id, user_token, expiry_date, username, server_url):
        try:
            # Create temp directory
            temp_dir = tempfile.mkdtemp()
            session_id = str(uuid.uuid4())
            working_dir = os.path.join(temp_dir, session_id)
            os.makedirs(working_dir, exist_ok=True)
            
            # Copy file to temp location
            source_path = os.path.join(working_dir, 'input.py')
            shutil.copy2(self.selected_file, source_path)
            
            # Encrypt the file
            result_file = elf(source_path, working_dir, self.protection_type, user_id, user_token, expiry_date, username, server_url)
            
            # Clean up
            shutil.rmtree(temp_dir, ignore_errors=True)
            
            self.status_label.text = f"Done! File saved to: {result_file}"
            self.error_label.text = ""
            
        except Exception as ex:
            self.error_label.text = f"Encryption failed: {str(ex)}"
            self.status_label.text = ""
        finally:
            self.encrypt_btn.text = "Encrypt Files"
            self.encrypt_btn.disabled = False
    
    def show_info_popup(self, instance):
        content = BoxLayout(orientation='vertical', spacing=10)
        
        info_text = """
Encryption Information

Advanced encryption system for Python files 
with multiple layers of protection.

Support Team:
First supporter: @LAEGER_MO
Second supporter: @sis_c
        """
        
        label = Label(text=info_text, color=get_color_from_hex('#eeeeee'))
        content.add_widget(label)
        
        close_btn = Button(text='Close', size_hint_y=None, height=50,
                         background_color=get_color_from_hex('#00cc99'))
        
        popup = Popup(title='Information', content=content,
                     size_hint=(0.8, 0.6))
        
        close_btn.bind(on_press=popup.dismiss)
        content.add_widget(close_btn)
        
        popup.open()

if __name__ == '__main__':
    NinjiGramProApp().run()
