import flet as ft
import os
import base64
import zipfile
import shutil
import tempfile
import subprocess
import uuid
import datetime
import sys

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

class NinjiGramProApp:
    def __init__(self):
        self.selected_file = None
        self.protection_type = "expiry"
        self.time_text = ft.Text("", size=18, color=ft.colors.TEAL_200)
        self.file_name_text = ft.Text("", color=ft.colors.WHITE)
        self.status_text = ft.Text("", color=ft.colors.GREEN)
        self.error_text = ft.Text("", color=ft.colors.RED)
        
    def update_time(self, e=None):
        now = datetime.datetime.now()
        self.time_text.value = now.strftime("%H:%M:%S")
        self.page.update()
    
    def on_file_selected(self, e: ft.FilePickerResultEvent):
        if e.files:
            self.selected_file = e.files[0].path
            self.file_name_text.value = f"Selected File: {e.files[0].name}"
            self.encrypt_btn.visible = True
            self.page.update()
    
    def on_protection_changed(self, e):
        self.protection_type = e.control.data
        # Update UI based on selection
        for option in self.protection_options:
            option.bgcolor = ft.colors.TEAL if option.data == self.protection_type else ft.colors.GREY_800
        self.expiry_section.visible = (self.protection_type == "expiry")
        self.server_section.visible = (self.protection_type == "server")
        self.page.update()
    
    def encrypt_file(self, e):
        if not self.selected_file:
            self.error_text.value = "Please select a file first"
            self.page.update()
            return
        
        user_id = self.user_id_field.value
        user_token = self.user_token_field.value
        
        if not user_id or not user_token:
            self.error_text.value = "ID and Token are required"
            self.page.update()
            return
        
        try:
            if self.protection_type == "expiry":
                expiry_date_str = self.expiry_date_field.value
                username = self.username_field.value
                if not expiry_date_str or not username:
                    self.error_text.value = "Expiry date and username are required"
                    self.page.update()
                    return
                expiry_date = datetime.datetime.strptime(expiry_date_str, '%Y-%m-%d').date()
                server_url = None
            else:  # server protection
                server_url = self.server_url_field.value
                if not server_url:
                    self.error_text.value = "Server URL is required"
                    self.page.update()
                    return
                expiry_date = None
                username = None
            
            # Show loading state
            self.encrypt_btn.text = "Encrypting..."
            self.encrypt_btn.disabled = True
            self.page.update()
            
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
            
            self.status_text.value = f"Done! File saved to: {result_file}"
            self.error_text.value = ""
            
        except Exception as ex:
            self.error_text.value = f"Encryption failed: {str(ex)}"
            self.status_text.value = ""
        finally:
            self.encrypt_btn.text = "Encrypt Files"
            self.encrypt_btn.disabled = False
            self.page.update()
    
    def build(self, page: ft.Page):
        self.page = page
        page.title = "NinjiGramPro Encryptor"
        page.theme_mode = ft.ThemeMode.DARK
        page.bgcolor = ft.colors.BLACK
        page.padding = 0
        
        # File picker
        self.file_picker = ft.FilePicker(on_result=self.on_file_selected)
        page.overlay.append(self.file_picker)
        
        # Header
        header = ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Row([
                        self.time_text,
                        ft.Container(
                            width=20, height=20, border_radius=10,
                            bgcolor=ft.colors.GREEN,
                            content=ft.Text("✓", size=12, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                            alignment=ft.alignment.center
                        )
                    ]),
                    padding=10
                ),
                ft.Container(
                    content=ft.Text(
                        "NinjiGramPro",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        gradient=ft.LinearGradient(
                            colors=[ft.colors.RED, ft.colors.WHITE, ft.colors.RED]
                        )
                    ),
                    animate_offset=ft.animation.Animation(3000, ft.AnimationCurve.BOUNCE_OUT),
                    offset=ft.transform.Offset(0, -0.1)
                ),
                ft.Container(
                    content=ft.IconButton(
                        icon=ft.icons.PERSON,
                        icon_color=ft.colors.TEAL_200,
                        icon_size=30,
                        on_click=lambda _: self.show_info_dialog()
                    )
                )
            ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            bgcolor=ft.colors.GREY_900,
            padding=15,
            border_radius=ft.border_radius.only(bottom_left=10, bottom_right=10)
        )
        
        # Main content
        self.user_id_field = ft.TextField(
            label="Your ID",
            hint_text="Enter your ID",
            border_color=ft.colors.GREY_600,
            filled=True,
            bgcolor=ft.colors.GREY_900
        )
        
        self.user_token_field = ft.TextField(
            label="Your Token",
            hint_text="Enter your token",
            border_color=ft.colors.GREY_600,
            filled=True,
            bgcolor=ft.colors.GREY_900
        )
        
        # Protection type selection
        self.protection_options = []
        expiry_option = ft.Container(
            content=ft.Text("Expiry Date Protection"),
            data="expiry",
            padding=15,
            border_radius=5,
            bgcolor=ft.colors.TEAL,
            on_click=self.on_protection_changed
        )
        
        server_option = ft.Container(
            content=ft.Text("Server Check Protection"),
            data="server",
            padding=15,
            border_radius=5,
            bgcolor=ft.colors.GREY_800,
            on_click=self.on_protection_changed
        )
        
        self.protection_options.extend([expiry_option, server_option])
        
        # Expiry section
        self.expiry_date_field = ft.TextField(
            label="Expiry Date (YYYY-MM-DD)",
            hint_text="2024-12-31",
            border_color=ft.colors.GREY_600,
            filled=True,
            bgcolor=ft.colors.GREY_900
        )
        
        self.username_field = ft.TextField(
            label="Your Username",
            hint_text="@your_username",
            border_color=ft.colors.GREY_600,
            filled=True,
            bgcolor=ft.colors.GREY_900
        )
        
        self.expiry_section = ft.Column([
            self.expiry_date_field,
            self.username_field,
            ft.Text("Tool will stop working after this date", size=12, color=ft.colors.GREY_400)
        ])
        
        # Server section
        self.server_url_field = ft.TextField(
            label="Server URL",
            hint_text="https://example.com/status.txt",
            border_color=ft.colors.GREY_600,
            filled=True,
            bgcolor=ft.colors.GREY_900
        )
        
        self.server_section = ft.Column([
            self.server_url_field,
            ft.Text("Tool will check this URL for 'ON' status", size=12, color=ft.colors.GREY_400)
        ], visible=False)
        
        # Encrypt button
        self.encrypt_btn = ft.ElevatedButton(
            "Encrypt Files",
            icon=ft.icons.LOCK,
            on_click=self.encrypt_file,
            visible=False,
            style=ft.ButtonStyle(
                bgcolor=ft.colors.TEAL,
                color=ft.colors.WHITE
            )
        )
        
        # Info sections
        how_to_use = ft.Container(
            content=ft.Column([
                ft.Text("How to Use", size=18, color=ft.colors.TEAL_200),
                ft.Text("1. Click 'Choose Python File' to select your file"),
                ft.Text("2. The file will be uploaded automatically"),
                ft.Text("3. Click 'Encrypt Files' to start encryption process"),
                ft.Text("4. Download your encrypted file when ready"),
            ]),
            bgcolor=ft.colors.GREY_900,
            padding=20,
            border_radius=10
        )
        
        copyright_info = ft.Container(
            content=ft.Column([
                ft.Text("Copyright & Credentials", size=18, color=ft.colors.TEAL_200),
                ft.Text("This software is developed by Plya_Team"),
                ft.Text("User ID: XXXXXX"),
                ft.Text("Token: ************"),
            ]),
            bgcolor=ft.colors.GREY_900,
            padding=20,
            border_radius=10
        )
        
        # Floating action button
        fab = ft.Container(
            content=ft.IconButton(
                icon=ft.icons.ADD,
                icon_color=ft.colors.WHITE,
                icon_size=30,
                on_click=lambda _: self.show_time_dialog()
            ),
            width=60, height=60,
            bgcolor=ft.colors.BLUE,
            border_radius=30,
            alignment=ft.alignment.center,
            right=20, bottom=20,
            animate_position=ft.animation.Animation(300, ft.AnimationCurve.EASE_OUT)
        )
        
        # Main layout
        main_content = ft.Container(
            content=ft.Column([
                ft.Text("Enc_NinjiGramPro By Plya_Team", size=20, weight=ft.FontWeight.BOLD),
                
                ft.ElevatedButton(
                    "Choose Python File",
                    icon=ft.icons.UPLOAD_FILE,
                    on_click=lambda _: self.file_picker.pick_files(
                        allowed_extensions=["py"],
                        dialog_title="Select Python File"
                    ),
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.TEAL,
                        color=ft.colors.WHITE,
                        padding=20
                    )
                ),
                
                ft.Container(content=self.file_name_text, padding=10),
                
                self.user_id_field,
                self.user_token_field,
                
                ft.Row(self.protection_options, alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                self.expiry_section,
                self.server_section,
                
                self.encrypt_btn,
                self.status_text,
                self.error_text,
                
                how_to_use,
                copyright_info
            ], scroll=ft.ScrollMode.ADAPTIVE),
            padding=20,
            alignment=ft.alignment.top_center
        )
        
        # Stack for FAB
        content_stack = ft.Stack([
            ft.Column([header, main_content]),
            ft.Container(content=fab, alignment=ft.alignment.bottom_right)
        ])
        
        # Start time updates
        self.update_time()
        page.run_task(self.update_time_loop)
        
        return content_stack
    
    async def update_time_loop(self):
        while True:
            self.update_time()
            await asyncio.sleep(1)
    
    def show_info_dialog(self):
        dialog = ft.AlertDialog(
            title=ft.Text("Encryption Information"),
            content=ft.Column([
                ft.Text("Advanced encryption system for Python files with multiple layers of protection."),
                ft.Text("Support Team:", weight=ft.FontWeight.BOLD),
                ft.Text("First supporter: @LAEGER_MO"),
                ft.Text("Second supporter: @sis_c"),
            ], tight=True),
            actions=[ft.TextButton("OK", on_click=lambda _: self.page.close(dialog))]
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()
    
    def show_time_dialog(self):
        now = datetime.datetime.now()
        dialog = ft.AlertDialog(
            title=ft.Text("Time Information"),
            content=ft.Column([
                ft.Text(f"Current Date: {now.strftime('%Y-%m-%d')}"),
                ft.Text(f"Current Time: {now.strftime('%H:%M:%S')}"),
                ft.Container(
                    content=ft.Column([
                        ft.Text("About Expiry System", weight=ft.FontWeight.BOLD),
                        ft.Text("The tool will automatically stop working after the expiry date you set."),
                        ft.Text("When expired, it will show your username and stop execution."),
                    ]),
                    bgcolor=ft.colors.GREY_900,
                    padding=10,
                    border_radius=5
                )
            ], tight=True),
            actions=[ft.TextButton("OK", on_click=lambda _: self.page.close(dialog))]
        )
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

def main(page: ft.Page):
    app = NinjiGramProApp()
    page.add(app.build(page))

if __name__ == "__main__":
    import asyncio
    ft.app(target=main)
