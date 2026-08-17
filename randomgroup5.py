import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
from datetime import datetime


class GroupRandomizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("สุ่มกลุ่มอัตโนมัติ")
        self.root.geometry("1250x800")
        self.root.minsize(1000, 650)

        self.dark_mode = False
        self.history = []
        self.current_groups = []

        # สีหลัก
        self.colors = {
            "blue": "#4285E8",
            "blue_dark": "#2563C7",
            "blue_light": "#EAF3FF",
            "green": "#55C99A",
            "orange": "#F6B52E",
            "purple": "#9A7BEA",
            "pink": "#E77BB5",
            "cyan": "#5DB8C7",
            "text": "#243B64",
            "gray": "#71809B",
            "bg": "#F5F9FF",
            "white": "#FFFFFF",
            "border": "#D9E5F5"
        }

        self.group_colors = [
            "#4285E8",
            "#55C99A",
            "#F6B52E",
            "#9A7BEA",
            "#E77BB5",
            "#5DB8C7",
            "#F08080",
            "#55A6E8",
            "#76C893",
            "#C084FC"
        ]

        self.setup_style()
        self.create_ui()

    # ---------------------------------------------------------
    # STYLE
    # ---------------------------------------------------------

    def setup_style(self):
        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Treeview",
            font=("Tahoma", 11),
            rowheight=35
        )

    # ---------------------------------------------------------
    # MAIN UI
    # ---------------------------------------------------------

    def create_ui(self):
        self.root.configure(bg=self.colors["bg"])

        # ---------------- LEFT SIDEBAR ----------------

        self.sidebar = tk.Frame(
            self.root,
            bg=self.colors["white"],
            width=260
        )
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Logo
        logo_frame = tk.Frame(
            self.sidebar,
            bg=self.colors["white"]
        )
        logo_frame.pack(fill="x", padx=20, pady=(25, 15))

        logo = tk.Label(
            logo_frame,
            text="🎲",
            font=("Segoe UI Emoji", 28),
            bg=self.colors["blue"],
            fg="white",
            width=2,
            height=1
        )
        logo.pack(side="left", padx=(0, 10))

        title_box = tk.Frame(
            logo_frame,
            bg=self.colors["white"]
        )
        title_box.pack(side="left")

        tk.Label(
            title_box,
            text="สุ่มกลุ่มอัตโนมัติ",
            font=("Tahoma", 14, "bold"),
            fg=self.colors["text"],
            bg=self.colors["white"]
        ).pack(anchor="w")

        tk.Label(
            title_box,
            text="จัดกลุ่มอย่างรวดเร็ว ง่าย และยุติธรรม",
            font=("Tahoma", 8),
            fg=self.colors["gray"],
            bg=self.colors["white"]
        ).pack(anchor="w")

        # Menu
        self.menu_buttons = {}

        self.add_menu_button("⌂", "หน้าหลัก", self.show_home, active=True)
        self.add_menu_button("◷", "ประวัติการสุ่ม", self.show_history)
        self.add_menu_button("▣", "บันทึกผล", self.save_result)
        self.add_menu_button("⚙", "ตั้งค่า", self.show_settings)

        # ---------------- MAIN ----------------

        self.main = tk.Frame(
            self.root,
            bg=self.colors["bg"]
        )
        self.main.pack(side="left", fill="both", expand=True)

        self.create_topbar()

        self.content = tk.Frame(
            self.main,
            bg=self.colors["bg"]
        )
        self.content.pack(fill="both", expand=True, padx=25, pady=(0, 20))

        self.show_home()

    # ---------------------------------------------------------
    # SIDEBAR
    # ---------------------------------------------------------

    def add_menu_button(self, icon, text, command, active=False):
        frame = tk.Frame(
            self.sidebar,
            bg=self.colors["blue"] if active else self.colors["white"],
            height=55
        )
        frame.pack(fill="x", padx=12, pady=4)
        frame.pack_propagate(False)

        button = tk.Button(
            frame,
            text=f"{icon}    {text}",
            font=("Tahoma", 11, "bold" if active else "normal"),
            anchor="w",
            bd=0,
            relief="flat",
            cursor="hand2",
            bg=self.colors["blue"] if active else self.colors["white"],
            fg="white" if active else self.colors["text"],
            activebackground=self.colors["blue_light"],
            command=command
        )
        button.pack(fill="both", expand=True, padx=10)

        self.menu_buttons[text] = (frame, button)

    def set_active_menu(self, name):
        for text, (frame, button) in self.menu_buttons.items():
            if text == name:
                frame.configure(bg=self.colors["blue"])
                button.configure(
                    bg=self.colors["blue"],
                    fg="white"
                )
            else:
                frame.configure(bg=self.colors["white"])
                button.configure(
                    bg=self.colors["white"],
                    fg=self.colors["text"]
                )

    # ---------------------------------------------------------
    # TOP BAR
    # ---------------------------------------------------------

    def create_topbar(self):
        topbar = tk.Frame(
            self.main,
            bg=self.colors["bg"],
            height=90
        )
        topbar.pack(fill="x", padx=25, pady=(15, 0))
        topbar.pack_propagate(False)

        title_frame = tk.Frame(
            topbar,
            bg=self.colors["bg"]
        )
        title_frame.pack(side="left", fill="y")

        tk.Label(
            title_frame,
            text="〰️  สุ่มกลุ่มอัตโนมัติ 〰️",
            font=("Tahoma", 24, "bold"),
            fg=self.colors["text"],
            bg=self.colors["bg"]
        ).pack(anchor="w")

        tk.Label(
            title_frame,
            text="จัดกลุ่มคนได้อย่างรวดเร็ว และเป็นธรรม",
            font=("Tahoma", 10),
            fg=self.colors["gray"],
            bg=self.colors["bg"]
        ).pack(anchor="w")

        # Dark mode button
        self.dark_button = tk.Button(
            topbar,
            text="☾",
            font=("Tahoma", 18),
            width=3,
            height=1,
            bg=self.colors["white"],
            fg=self.colors["text"],
            bd=1,
            relief="solid",
            cursor="hand2",
            command=self.toggle_dark_mode
        )
        self.dark_button.pack(side="right", padx=(10, 0), pady=10)

        settings_button = tk.Button(
            topbar,
            text="⚙  ตั้งค่า",
            font=("Tahoma", 10, "bold"),
            bg=self.colors["white"],
            fg=self.colors["text"],
            bd=1,
            relief="solid",
            padx=15,
            cursor="hand2",
            command=self.show_settings
        )
        settings_button.pack(side="right", pady=10)

    # ---------------------------------------------------------
    # HOME
    # ---------------------------------------------------------

    def show_home(self):
        self.set_active_menu("หน้าหลัก")

        for widget in self.content.winfo_children():
            widget.destroy()

        # Input card
        input_card = tk.Frame(
            self.content,
            bg=self.colors["white"],
            highlightbackground=self.colors["border"],
            highlightthickness=1
        )
        input_card.pack(fill="x", pady=(0, 20))

        # Input layout
        input_inner = tk.Frame(
            input_card,
            bg=self.colors["white"]
        )
        input_inner.pack(fill="x", padx=25, pady=20)

        # จำนวนคน
        self.create_input_box(
            input_inner,
            "👤",
            "กรอกจำนวนคน",
            "คน",
            "30",
            0
        )

        # จำนวนกลุ่ม
        self.create_input_box(
            input_inner,
            "👥",
            "กรอกจำนวนกลุ่ม",
            "กลุ่ม",
            "6",
            1
        )

        # จำนวนคนต่อกลุ่ม
        result_box = tk.Frame(
            input_inner,
            bg="#EFF6FF",
            highlightbackground="#C9DEFA",
            highlightthickness=1
        )
        result_box.grid(
            row=0,
            column=2,
            padx=10,
            sticky="nsew"
        )

        input_inner.grid_columnconfigure(0, weight=1)
        input_inner.grid_columnconfigure(1, weight=1)
        input_inner.grid_columnconfigure(2, weight=1)
        input_inner.grid_columnconfigure(3, weight=1)

        tk.Label(
            result_box,
            text="👥",
            font=("Segoe UI Emoji", 20),
            bg="#EFF6FF"
        ).pack(side="left", padx=15, pady=15)

        result_text = tk.Frame(
            result_box,
            bg="#EFF6FF"
        )
        result_text.pack(side="left", pady=10)

        tk.Label(
            result_text,
            text="กลุ่มที่ได้",
            font=("Tahoma", 9),
            fg=self.colors["blue"],
            bg="#EFF6FF"
        ).pack(anchor="w")

        self.group_info_label = tk.Label(
            result_text,
            text="กลุ่มละ 5 คน",
            font=("Tahoma", 14, "bold"),
            fg=self.colors["text"],
            bg="#EFF6FF"
        )
        self.group_info_label.pack(anchor="w")

        # Random button
        random_button = tk.Button(
            input_inner,
            text="🪄  สุ่มกลุ่ม",
            font=("Tahoma", 14, "bold"),
            bg=self.colors["blue"],
            fg="white",
            activebackground=self.colors["blue_dark"],
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2",
            command=self.randomize
        )
        random_button.grid(
            row=0,
            column=3,
            padx=(10, 0),
            sticky="nsew"
        )

        # ---------------- RESULT TITLE ----------------

        result_title = tk.Frame(
            self.content,
            bg=self.colors["bg"]
        )
        result_title.pack(fill="x", pady=(0, 10))

        tk.Label(
            result_title,
            text="⟶   ผลลัพธ์กลุ่มที่ได้   ⟵",
            font=("Tahoma", 16, "bold"),
            fg=self.colors["text"],
            bg=self.colors["bg"]
        ).pack()

        # ---------------- RESULT AREA ----------------

        self.result_area = tk.Frame(
            self.content,
            bg=self.colors["bg"]
        )
        self.result_area.pack(
            fill="both",
            expand=True
        )

        # Initial result
        if self.current_groups:
            self.display_groups()
        else:
            self.display_empty()

        # Bottom buttons
        bottom = tk.Frame(
            self.content,
            bg=self.colors["bg"]
        )
        bottom.pack(fill="x", pady=(15, 0))

        tk.Button(
            bottom,
            text="⇩  บันทึกผลเป็นไฟล์",
            font=("Tahoma", 11, "bold"),
            bg=self.colors["white"],
            fg=self.colors["text"],
            bd=1,
            relief="solid",
            padx=25,
            pady=8,
            cursor="hand2",
            command=self.save_result
        ).pack(side="left", padx=(0, 10))

        tk.Button(
            bottom,
            text="⟳  สุ่มใหม่อีกครั้ง",
            font=("Tahoma", 11, "bold"),
            bg=self.colors["white"],
            fg=self.colors["text"],
            bd=1,
            relief="solid",
            padx=25,
            pady=8,
            cursor="hand2",
            command=self.randomize
        ).pack(side="left")

    # ---------------------------------------------------------
    # INPUT BOX
    # ---------------------------------------------------------

    def create_input_box(
        self,
        parent,
        icon,
        title,
        unit,
        default,
        column
    ):
        box = tk.Frame(
            parent,
            bg=self.colors["white"],
            highlightbackground=self.colors["border"],
            highlightthickness=1
        )
        box.grid(
            row=0,
            column=column,
            padx=10,
            sticky="nsew"
        )

        tk.Label(
            box,
            text=icon,
            font=("Segoe UI Emoji", 20),
            bg=self.colors["white"]
        ).pack(side="left", padx=12)

        middle = tk.Frame(
            box,
            bg=self.colors["white"]
        )
        middle.pack(side="left", fill="both", expand=True)

        tk.Label(
            middle,
            text=title,
            font=("Tahoma", 9, "bold"),
            fg=self.colors["text"],
            bg=self.colors["white"]
        ).pack(anchor="w", pady=(10, 0))

        entry_frame = tk.Frame(
            middle,
            bg=self.colors["white"]
        )
        entry_frame.pack(fill="x", pady=(0, 10))

        entry = tk.Entry(
            entry_frame,
            font=("Tahoma", 16, "bold"),
            fg=self.colors["text"],
            bg=self.colors["white"],
            bd=0,
            width=8
        )
        entry.insert(0, default)
        entry.pack(side="left")

        tk.Label(
            entry_frame,
            text=unit,
            font=("Tahoma", 10),
            fg=self.colors["gray"],
            bg=self.colors["white"]
        ).pack(side="left", padx=5)

        if column == 0:
            self.people_entry = entry
            entry.bind("<KeyRelease>", self.update_group_info)

        elif column == 1:
            self.groups_entry = entry
            entry.bind("<KeyRelease>", self.update_group_info)

    # ---------------------------------------------------------
    # CALCULATE GROUP SIZE
    # ---------------------------------------------------------

    def update_group_info(self, event=None):
        try:
            people = int(self.people_entry.get())
            groups = int(self.groups_entry.get())

            if groups > 0:
                base = people // groups
                remainder = people % groups

                if remainder == 0:
                    text = f"กลุ่มละ {base} คน"
                else:
                    text = f"กลุ่มละ {base}-{base + 1} คน"

                self.group_info_label.config(text=text)
        except:
            self.group_info_label.config(text="กรอกข้อมูลให้ถูกต้อง")

    # ---------------------------------------------------------
    # RANDOMIZE
    # ---------------------------------------------------------

    def randomize(self):
        try:
            people = int(self.people_entry.get())
            groups = int(self.groups_entry.get())

        except ValueError:
            messagebox.showerror(
                "ข้อมูลไม่ถูกต้อง",
                "กรุณากรอกจำนวนคนและจำนวนกลุ่มเป็นตัวเลข"
            )
            return

        if people <= 0:
            messagebox.showerror(
                "ข้อมูลไม่ถูกต้อง",
                "จำนวนคนต้องมากกว่า 0"
            )
            return

        if groups <= 0:
            messagebox.showerror(
                "ข้อมูลไม่ถูกต้อง",
                "จำนวนกลุ่มต้องมากกว่า 0"
            )
            return

        if groups > people:
            messagebox.showerror(
                "ข้อมูลไม่ถูกต้อง",
                "จำนวนกลุ่มต้องไม่มากกว่าจำนวนคน"
            )
            return

        # สร้างเลขที่
        numbers = list(range(1, people + 1))

        # สุ่ม
        random.shuffle(numbers)

        # สร้างกลุ่ม
        result = [[] for _ in range(groups)]

        # กระจายแบบวนรอบ
        for index, number in enumerate(numbers):
            result[index % groups].append(number)

        # สุ่มลำดับกลุ่มอีกครั้ง
        random.shuffle(result)

        self.current_groups = result

        # เก็บประวัติ
        self.history.append({
            "time": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "people": people,
            "groups": groups,
            "result": [g[:] for g in result]
        })

        self.display_groups()

    # ---------------------------------------------------------
    # DISPLAY EMPTY
    # ---------------------------------------------------------

    def display_empty(self):
        for widget in self.result_area.winfo_children():
            widget.destroy()

        empty = tk.Frame(
            self.result_area,
            bg=self.colors["white"],
            highlightbackground=self.colors["border"],
            highlightthickness=1
        )
        empty.pack(
            fill="both",
            expand=True,
            padx=5
        )

        tk.Label(
            empty,
            text="🎲",
            font=("Segoe UI Emoji", 45),
            bg=self.colors["white"]
        ).pack(pady=(50, 10))

        tk.Label(
            empty,
            text="กดปุ่ม “สุ่มกลุ่ม” เพื่อเริ่มต้น",
            font=("Tahoma", 14, "bold"),
            fg=self.colors["text"],
            bg=self.colors["white"]
        ).pack()

        tk.Label(
            empty,
            text="ระบบจะสุ่มเลขที่และแบ่งกลุ่มให้อัตโนมัติ",
            font=("Tahoma", 10),
            fg=self.colors["gray"],
            bg=self.colors["white"]
        ).pack(pady=5)

    # ---------------------------------------------------------
    # DISPLAY GROUPS
    # ---------------------------------------------------------

    def display_groups(self):
        for widget in self.result_area.winfo_children():
            widget.destroy()

        if not self.current_groups:
            self.display_empty()
            return

        # Canvas + scrollbar
        canvas = tk.Canvas(
            self.result_area,
            bg=self.colors["bg"],
            highlightthickness=0
        )
        canvas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar = ttk.Scrollbar(
            self.result_area,
            orient="vertical",
            command=canvas.yview
        )
        scrollbar.pack(
            side="right",
            fill="y"
        )

        container = tk.Frame(
            canvas,
            bg=self.colors["bg"]
        )

        window_id = canvas.create_window(
            (0, 0),
            window=container,
            anchor="nw"
        )

        def configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(window_id, width=event.width)

        container.bind("<Configure>", configure)
        canvas.bind("<Configure>", configure)

        # จำนวนคอลัมน์
        group_count = len(self.current_groups)

        if group_count <= 2:
            columns = 2
        elif group_count <= 6:
            columns = 3
        elif group_count <= 12:
            columns = 4
        else:
            columns = 5

        for i, group in enumerate(self.current_groups):
            row = i // columns
            col = i % columns

            card = self.create_group_card(
                container,
                i + 1,
                group
            )

            card.grid(
                row=row,
                column=col,
                padx=7,
                pady=7,
                sticky="nsew"
            )

        for col in range(columns):
            container.grid_columnconfigure(
                col,
                weight=1
            )

        # Mouse wheel
        def mousewheel(event):
            canvas.yview_scroll(
                int(-1 * (event.delta / 120)),
                "units"
            )

        canvas.bind_all("<MouseWheel>", mousewheel)

    # ---------------------------------------------------------
    # GROUP CARD
    # ---------------------------------------------------------

    def create_group_card(self, parent, group_number, members):
        color = self.group_colors[
            (group_number - 1) % len(self.group_colors)
        ]

        card = tk.Frame(
            parent,
            bg=self.colors["white"],
            highlightbackground=color,
            highlightthickness=1
        )

        # Header
        header = tk.Frame(
            card,
            bg=color,
            height=42
        )
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text=f"กลุ่มที่ {group_number}",
            font=("Tahoma", 11, "bold"),
            bg=color,
            fg="white"
        ).pack(side="left", padx=12)

        tk.Label(
            header,
            text="👥",
            font=("Segoe UI Emoji", 14),
            bg=color,
            fg="white"
        ).pack(side="right", padx=10)

        # Members
        for index, number in enumerate(members):
            row = tk.Frame(
                card,
                bg=self.colors["white"]
            )
            row.pack(fill="x")

            tk.Label(
                row,
                text=f"{index + 1}.",
                font=("Tahoma", 10),
                fg=self.colors["gray"],
                bg=self.colors["white"],
                width=4,
                anchor="e"
            ).pack(side="left", padx=(5, 0), pady=5)

            tk.Label(
                row,
                text=f"เลขที่ {number}",
                font=("Tahoma", 10),
                fg=self.colors["text"],
                bg=self.colors["white"],
                anchor="w"
            ).pack(
                side="left",
                padx=8,
                pady=5
            )

        return card

    # ---------------------------------------------------------
    # SAVE RESULT
    # ---------------------------------------------------------

    def save_result(self):
        if not self.current_groups:
            messagebox.showwarning(
                "ยังไม่มีผลลัพธ์",
                "กรุณาสุ่มกลุ่มก่อนบันทึกผล"
            )
            return

        filename = filedialog.asksaveasfilename(
            title="บันทึกผลการสุ่ม",
            defaultextension=".txt",
            filetypes=[
                ("Text File", "*.txt"),
                ("All Files", "*.*")
            ]
        )

        if not filename:
            return

        try:
            with open(
                filename,
                "w",
                encoding="utf-8"
            ) as file:

                file.write("=================================\n")
                file.write("       ผลการสุ่มกลุ่มอัตโนมัติ\n")
                file.write("=================================\n\n")

                file.write(
                    f"วันที่: "
                    f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
                )

                file.write(
                    f"จำนวนคน: "
                    f"{sum(len(g) for g in self.current_groups)} คน\n"
                )

                file.write(
                    f"จำนวนกลุ่ม: "
                    f"{len(self.current_groups)} กลุ่ม\n\n"
                )

                for i, group in enumerate(
                    self.current_groups,
                    start=1
                ):
                    file.write(f"กลุ่มที่ {i}\n")

                    for j, number in enumerate(
                        group,
                        start=1
                    ):
                        file.write(
                            f"  {j}. เลขที่ {number}\n"
                        )

                    file.write("\n")

            messagebox.showinfo(
                "บันทึกสำเร็จ",
                "บันทึกผลการสุ่มเรียบร้อยแล้ว"
            )

        except Exception as e:
            messagebox.showerror(
                "เกิดข้อผิดพลาด",
                str(e)
            )

    # ---------------------------------------------------------
    # HISTORY
    # ---------------------------------------------------------

    def show_history(self):
        self.set_active_menu("ประวัติการสุ่ม")

        for widget in self.content.winfo_children():
            widget.destroy()

        tk.Label(
            self.content,
            text="ประวัติการสุ่ม",
            font=("Tahoma", 20, "bold"),
            fg=self.colors["text"],
            bg=self.colors["bg"]
        ).pack(anchor="w", pady=(10, 20))

        if not self.history:
            box = tk.Frame(
                self.content,
                bg=self.colors["white"],
                highlightbackground=self.colors["border"],
                highlightthickness=1
            )
            box.pack(fill="both", expand=True)

            tk.Label(
                box,
                text="ยังไม่มีประวัติการสุ่ม",
                font=("Tahoma", 14),
                fg=self.colors["gray"],
                bg=self.colors["white"]
            ).pack(expand=True)

            return

        # History list
        for index, item in enumerate(
            reversed(self.history),
            start=1
        ):
            card = tk.Frame(
                self.content,
                bg=self.colors["white"],
                highlightbackground=self.colors["border"],
                highlightthickness=1
            )
            card.pack(
                fill="x",
                pady=5
            )

            text = (
                f"ครั้งที่ {index}     "
                f"{item['time']}     |     "
                f"{item['people']} คน     |     "
                f"{item['groups']} กลุ่ม"
            )

            tk.Label(
                card,
                text=text,
                font=("Tahoma", 11),
                fg=self.colors["text"],
                bg=self.colors["white"]
            ).pack(
                side="left",
                padx=15,
                pady=15
            )

            result = item["result"]

            tk.Button(
                card,
                text="ดูผล",
                font=("Tahoma", 9, "bold"),
                bg=self.colors["blue"],
                fg="white",
                bd=0,
                cursor="hand2",
                command=lambda r=result: self.load_history(r)
            ).pack(
                side="right",
                padx=15
            )

    def load_history(self, result):
        self.current_groups = [g[:] for g in result]
        self.show_home()

    # ---------------------------------------------------------
    # SETTINGS
    # ---------------------------------------------------------

    def show_settings(self):
        self.set_active_menu("ตั้งค่า")

        for widget in self.content.winfo_children():
            widget.destroy()

        tk.Label(
            self.content,
            text="ตั้งค่า",
            font=("Tahoma", 20, "bold"),
            fg=self.colors["text"],
            bg=self.colors["bg"]
        ).pack(anchor="w", pady=(10, 20))

        card = tk.Frame(
            self.content,
            bg=self.colors["white"],
            highlightbackground=self.colors["border"],
            highlightthickness=1
        )
        card.pack(fill="x")

        # Random mode
        tk.Label(
            card,
            text="รูปแบบการสุ่ม",
            font=("Tahoma", 12, "bold"),
            fg=self.colors["text"],
            bg=self.colors["white"]
        ).pack(anchor="w", padx=25, pady=(20, 5))

        tk.Label(
            card,
            text="สุ่มเลขที่และกระจายสมาชิกให้แต่ละกลุ่มใกล้เคียงกันที่สุด",
            font=("Tahoma", 10),
            fg=self.colors["gray"],
            bg=self.colors["white"]
        ).pack(anchor="w", padx=25)

        # Clear history
        tk.Button(
            card,
            text="ล้างประวัติการสุ่ม",
            font=("Tahoma", 10, "bold"),
            bg="#FFECEC",
            fg="#D64545",
            bd=0,
            cursor="hand2",
            padx=20,
            pady=10,
            command=self.clear_history
        ).pack(
            anchor="w",
            padx=25,
            pady=25
        )

    def clear_history(self):
        if not self.history:
            messagebox.showinfo(
                "ประวัติ",
                "ไม่มีประวัติให้ล้าง"
            )
            return

        confirm = messagebox.askyesno(
            "ยืนยัน",
            "คุณต้องการล้างประวัติทั้งหมดหรือไม่?"
        )

        if confirm:
            self.history.clear()
            messagebox.showinfo(
                "สำเร็จ",
                "ล้างประวัติเรียบร้อยแล้ว"
            )
            self.show_history()

    # ---------------------------------------------------------
    # DARK MODE
    # ---------------------------------------------------------

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            self.colors["bg"] = "#111827"
            self.colors["white"] = "#1F2937"
            self.colors["text"] = "#F3F4F6"
            self.colors["gray"] = "#AAB4C3"
            self.colors["border"] = "#374151"

            self.dark_button.config(text="☀")
        else:
            self.colors["bg"] = "#F5F9FF"
            self.colors["white"] = "#FFFFFF"
            self.colors["text"] = "#243B64"
            self.colors["gray"] = "#71809B"
            self.colors["border"] = "#D9E5F5"

            self.dark_button.config(text="☾")

        # สร้างหน้าปัจจุบันใหม่
        if self.menu_buttons["หน้าหลัก"][1].cget("fg") == "white":
            self.show_home()
        else:
            self.show_home()


# ---------------------------------------------------------
# START APP
# ---------------------------------------------------------

if __name__ == "__main__":
    root = tk.Tk()

    app = GroupRandomizerApp(root)

    root.mainloop()
    

