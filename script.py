from tkinter import messagebox, ttk
from tkinter import *
from fpdf import FPDF
import pyqrcode
import os

from tkinter import messagebox, ttk
from tkinter import *
from fpdf import FPDF
import os

class PDFCV(FPDF):
    def __init__(self):
        super().__init__()
        self.qr_code_size = 25  # Smaller QR code size
        self.right_margin = 10  # Right margin for QR code
        
    def header(self):
        # Add QR code on the right side if exists
        qr_path = os.path.abspath("mywebsite.png")
        if os.path.exists(qr_path):
            self.image(qr_path, 
                     x=self.w - self.qr_code_size - self.right_margin, 
                     y=10,  # Slightly lower than top edge
                     w=self.qr_code_size, 
                     h=self.qr_code_size)
    
    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    def generate_cv(self, personal_info, education, work_experience, skills, languages, 
                   projects, certifications, references):
        self.add_page()
        self.ln(10)
        
        # Personal information
        self.set_font("helvetica", "B", 26)
        self.cell(0, 10, personal_info["name"], new_x="LMARGIN", new_y="NEXT", align="C")
        
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "CONTACT", new_x="LMARGIN", new_y="NEXT", align="L")
        self.set_font("helvetica", "", 10)
        
        self.cell(0, 5, f"Phone: {personal_info['phone']}", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 5, f"Email: {personal_info['email']}", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 5, f"LinkedIn: {personal_info['linkedin']}", new_x="LMARGIN", new_y="NEXT")
        self.cell(0, 5, f"Address: {personal_info['address']}", new_x="LMARGIN", new_y="NEXT")
        
        # Education
        self.ln(5)
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "EDUCATION", new_x="LMARGIN", new_y="NEXT", align="L")
        self.set_font("helvetica", "", 10)
        
        for edu in education:
            if edu.get("degree") and edu.get("institution"):
                self.set_font("helvetica", "B", 10)
                self.cell(0, 5, f"{edu['degree']}", new_x="LMARGIN", new_y="NEXT")
                self.set_font("helvetica", "", 10)
                self.cell(0, 5, f"{edu['institution']} | {edu['period']}", new_x="LMARGIN", new_y="NEXT")
                if edu.get("cgpa"):
                    self.cell(0, 5, f"CGPA: {edu['cgpa']}", new_x="LMARGIN", new_y="NEXT")
                self.ln(2)

        # Work Experience (using dashes instead of bullets)
        self.ln(5)
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "WORK EXPERIENCE", new_x="LMARGIN", new_y="NEXT", align="L")
        
        for exp in work_experience:
            if exp.get("title") and exp.get("company"):
                self.set_font("helvetica", "B", 10)
                self.cell(0, 5, f"{exp['title']} | {exp['period']}", new_x="LMARGIN", new_y="NEXT")
                self.set_font("helvetica", "I", 10)
                self.cell(0, 5, exp['company'], new_x="LMARGIN", new_y="NEXT")
                self.set_font("helvetica", "", 10)
                for desc in exp['description'].split('\n'):
                    if desc.strip():
                        self.cell(0, 5, f"- {desc.strip()}", new_x="LMARGIN", new_y="NEXT")  # Dash instead of bullet
                if exp.get("portfolio"):
                    self.cell(0, 5, f"Portfolio: {exp['portfolio']}", new_x="LMARGIN", new_y="NEXT")
                self.ln(2)

        # Skills
        self.ln(5)
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "SKILLS SUMMARY", new_x="LMARGIN", new_y="NEXT", align="L")
        self.set_font("helvetica", "", 10)
        
        # Check if skills is a dictionary
        if isinstance(skills, dict):
            for category, skills_list in skills.items():
                if skills_list and str(skills_list).strip():
                    self.cell(0, 5, f"{category}: {skills_list}", new_x="LMARGIN", new_y="NEXT")
        else:
            # Fallback if skills is a string
            self.multi_cell(0, 5, f"Skills: {str(skills)}", new_x="LMARGIN", new_y="NEXT")

        # Languages
        self.ln(5)
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "LANGUAGES", new_x="LMARGIN", new_y="NEXT", align="L")
        self.set_font("helvetica", "", 10)
        
        for language in languages:
            if language.strip():
                self.cell(0, 5, f"- {language}", new_x="LMARGIN", new_y="NEXT")  # Dash instead of bullet

        # Projects (using dashes instead of bullets)
        self.ln(5)
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "PROJECTS", new_x="LMARGIN", new_y="NEXT", align="L")
        
        for project in projects:
            if project.get("name") and project.get("description"):
                self.set_font("helvetica", "B", 10)
                self.cell(0, 5, f"{project['name']} ({project['technologies']})", new_x="LMARGIN", new_y="NEXT")
                self.set_font("helvetica", "", 10)
                for desc in project['description'].split('\n'):
                    if desc.strip():
                        self.cell(0, 5, f"- {desc.strip()}", new_x="LMARGIN", new_y="NEXT")  # Dash instead of bullet
                if project.get("link"):
                    self.cell(0, 5, f"Project: {project['link']}", new_x="LMARGIN", new_y="NEXT")
                self.ln(2)

        # Certifications
        self.ln(5)
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "CERTIFICATIONS", new_x="LMARGIN", new_y="NEXT", align="L")
        
        for cert in certifications:
            if cert.get("name") and cert.get("issuer"):
                self.set_font("helvetica", "B", 10)
                self.cell(0, 5, f"{cert['name']} ({cert['issuer']})", new_x="LMARGIN", new_y="NEXT")
                self.set_font("helvetica", "", 10)
                if cert.get("description"):
                    for line in cert['description'].split('\n'):
                        if line.strip():
                            self.cell(0, 5, f"- {line.strip()}", new_x="LMARGIN", new_y="NEXT")  # Dash instead of bullet
                if cert.get("skills"):
                    self.cell(0, 5, f"Skills: {cert['skills']}", new_x="LMARGIN", new_y="NEXT")
                self.ln(2)

        # References
        self.ln(5)
        self.set_font("helvetica", "B", 12)
        self.cell(0, 10, "REFERENCES", new_x="LMARGIN", new_y="NEXT", align="L")
        
        for ref in references:
            if ref.get("name") and ref.get("position"):
                self.set_font("helvetica", "B", 10)
                self.cell(0, 5, ref['name'], new_x="LMARGIN", new_y="NEXT")
                self.set_font("helvetica", "I", 10)
                self.cell(0, 5, f"{ref['position']}", new_x="LMARGIN", new_y="NEXT")
                self.set_font("helvetica", "", 10)
                if ref.get("contact"):
                    self.cell(0, 5, f"Contact: {ref['contact']}", new_x="LMARGIN", new_y="NEXT")
                if ref.get("email"):
                    self.cell(0, 5, f"Email: {ref['email']}", new_x="LMARGIN", new_y="NEXT")
                if ref.get("linkedin"):
                    self.cell(0, 5, f"LinkedIn: {ref['linkedin']}", new_x="LMARGIN", new_y="NEXT")
                self.ln(2)

        output_path = os.path.abspath("mycv.pdf")
        self.output(output_path)
        return output_path
    

def generate_cv_pdf():
    try:
        # Create PDF with unicode font support
        pdf = PDFCV()
        # Important: Set UTF-8 encoding
        pdf.set_auto_page_break(auto=True, margin=15)
        
        # Get personal information
        personal_info = {
            "name": entry_name.get().strip(),
            "email": entry_email.get().strip(),
            "phone": entry_phone.get().strip(),
            "address": entry_address.get().strip(),
            "linkedin": entry_linkedin.get().strip()
        }
        
        # Validate required fields
        if not all([personal_info["name"], personal_info["email"], personal_info["phone"]]):
            messagebox.showerror("Error", "Please fill in all required personal information fields.")
            return

        # Process education
        education = []
        for entry in education_entries:
            degree = entry["degree"].get().strip()
            institution = entry["institution"].get().strip()
            period = entry["period"].get().strip()
            cgpa = entry["cgpa"].get().strip()
            
            if degree and institution:
                education.append({
                    "degree": degree,
                    "institution": institution,
                    "period": period,
                    "cgpa": cgpa
                })
        
        # Process work experience
        work_experience = []
        for entry in experience_entries:
            title = entry["title"].get().strip()
            company = entry["company"].get().strip()
            period = entry["period"].get().strip()
            description = entry["description"].get("1.0", END).strip()
            portfolio = entry["portfolio"].get().strip()
            
            if title and company:
                work_experience.append({
                    "title": title,
                    "company": company,
                    "period": period,
                    "description": description,
                    "portfolio": portfolio
                })
        
        # Process skills
        skills_dict = {
            "Languages": entry_languages_skills.get().strip(),
            "Frameworks": entry_frameworks_skills.get().strip(),
            "Tools": entry_tools_skills.get().strip(),
            "Platforms": entry_platforms_skills.get().strip()
        }
        
        # Process languages
        languages = [lang.strip() for lang in entry_languages.get("1.0", END).strip().split('\n') if lang.strip()]
        
        # Process projects
        projects = []
        for entry in project_entries:
            name = entry["name"].get().strip()
            technologies = entry["technologies"].get().strip()
            description = entry["description"].get("1.0", END).strip()
            link = entry["link"].get().strip()
            
            if name and description:
                projects.append({
                    "name": name,
                    "technologies": technologies,
                    "description": description,
                    "link": link
                })
        
        # Process certifications
        certifications = []
        for entry in certification_entries:
            name = entry["name"].get().strip()
            issuer = entry["issuer"].get().strip()
            description = entry["description"].get("1.0", END).strip()
            skills = entry["skills"].get().strip()
            
            if name and issuer:
                certifications.append({
                    "name": name,
                    "issuer": issuer,
                    "description": description,
                    "skills": skills
                })
        
        # Process references
        references = []
        for entry in reference_entries:
            name = entry["name"].get().strip()
            position = entry["position"].get().strip()
            contact = entry["contact"].get().strip()
            email = entry["email"].get().strip()
            linkedin = entry["linkedin"].get().strip()
            
            if name and position:
                references.append({
                    "name": name,
                    "position": position,
                    "contact": contact,
                    "email": email,
                    "linkedin": linkedin
                })

        # Generate QR code with absolute path if website provided
        website = entry_website.get().strip()
        if website:
            qr_path = os.path.abspath("D:/Python Course/Just for trial folder/mywebsite.png")
            try:
                qrcode = pyqrcode.create(website)
                qrcode.png(qr_path, scale=6)
            except Exception as e:
                messagebox.showwarning("Warning", f"Couldn't generate QR code: {str(e)}")

        # Generate PDF
        output_path = pdf.generate_cv(personal_info, education, work_experience, skills_dict,
                                    languages, projects, certifications, references)
        
        # Show success message
        success_window = Toplevel(window)
        success_window.title("Success")
        success_window.geometry("400x150")
        success_window.configure(bg="#f0f0f0")
        
        frame = Frame(success_window, bg="#f0f0f0")
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        Label(frame, text="CV Generated Successfully!", font=("Segoe UI", 14, "bold"), bg="#f0f0f0").pack(pady=10)
        Label(frame, text=f"Saved to: {output_path}", font=("Segoe UI", 10), bg="#f0f0f0", wraplength=350).pack()
        
        Button(frame, text="OK", command=success_window.destroy, font=("Segoe UI", 10), 
              bg="#4caf50", fg="white", width=10, cursor="hand2").pack(pady=10)
        
        # Center window
        success_window.update_idletasks()
        width = success_window.winfo_width()
        height = success_window.winfo_height()
        x = (success_window.winfo_screenwidth() // 2) - (width // 2)
        y = (success_window.winfo_screenheight() // 2) - (height // 2)
        success_window.geometry(f"{width}x{height}+{x}+{y}")
        success_window.focus_set()
    
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Set custom style
def set_app_style():
    # Configure theme colors
    window.configure(bg="#f0f0f0")
    
    # Custom font
    default_font = ("Segoe UI", 10)
    heading_font = ("Segoe UI", 11, "bold")
    
    # Custom colors
    primary_color = "#1976d2"  # Blue
    secondary_color = "#f0f0f0"  # Light gray
    accent_color = "#4caf50"  # Green
    
    return default_font, heading_font, primary_color, secondary_color, accent_color

# Create custom entry widget with label
def create_entry_with_label(parent, label_text, row, required=False):
    frame = Frame(parent, bg=secondary_color)
    frame.grid(row=row, column=0, sticky="ew", padx=5, pady=5)
    parent.grid_columnconfigure(0, weight=1)
    
    label = label_text + " *" if required else label_text
    Label(frame, text=label, font=default_font, bg=secondary_color, fg="#333333", width=12, anchor="w").pack(side=LEFT)
    
    entry = Entry(frame, font=default_font, bg="white", fg="#333333", relief="solid", bd=1)
    entry.pack(side=LEFT, fill="x", expand=True, padx=(5, 0))
    
    return entry

# Create text area with label frame
def create_text_area(parent, label_text, height=5):
    frame = LabelFrame(parent, text=label_text, font=heading_font, bg=secondary_color, fg=primary_color, bd=1, relief="solid", padx=10, pady=10)
    frame.pack(fill="x", padx=15, pady=10)
    
    text_widget = Text(frame, height=height, font=default_font, bg="white", fg="#333333", relief="solid", bd=1)
    text_widget.pack(fill="x", expand=True)
    
    scrollbar = ttk.Scrollbar(frame, command=text_widget.yview)
    scrollbar.place(relheight=1, relx=1, x=-5)
    text_widget['yscrollcommand'] = scrollbar.set
    
    return text_widget

# Dynamic sections for multiple entries
def create_dynamic_section(parent, title, fields, add_button_text="Add New"):
    frame = LabelFrame(parent, text=title, font=heading_font, bg=secondary_color, fg=primary_color, bd=1, relief="solid")
    frame.pack(fill="x", padx=15, pady=10)
    
    entries_frame = Frame(frame, bg=secondary_color)
    entries_frame.pack(fill="x", expand=True, padx=10, pady=5)
    
    entries = []
    
    def add_entry():
        entry_frame = Frame(entries_frame, bg=secondary_color, bd=1, relief="solid")
        entry_frame.pack(fill="x", padx=5, pady=5)
        
        entry_dict = {}
        for i, (field_name, config) in enumerate(fields.items()):
            field_frame = Frame(entry_frame, bg=secondary_color)
            field_frame.pack(fill="x", padx=5, pady=2)
            
            Label(field_frame, text=field_name, font=default_font, bg=secondary_color, width=12, anchor="w").pack(side=LEFT)
            
            if config.get("multiline", False):
                text_widget = Text(field_frame, height=config.get("height", 3), font=default_font, bg="white", relief="solid", bd=1)
                text_widget.pack(side=LEFT, fill="x", expand=True)
                entry_dict[config.get("key", field_name.lower())] = text_widget
            else:
                entry_widget = Entry(field_frame, font=default_font, bg="white", relief="solid", bd=1)
                entry_widget.pack(side=LEFT, fill="x", expand=True)
                entry_dict[config.get("key", field_name.lower())] = entry_widget
        
        # Add remove button
        remove_btn = Button(
            entry_frame, 
            text="✕", 
            command=lambda f=entry_frame, e=entry_dict: remove_entry(f, e),
            bg="#f44336", 
            fg="white", 
            font=("Segoe UI", 8),
            width=2,
            relief="flat",
            cursor="hand2"
        )
        remove_btn.pack(anchor="ne", padx=5, pady=5)
        
        entries.append(entry_dict)
        return entry_dict
    
    def remove_entry(frame, entry_dict):
        if frame in entries_frame.winfo_children():
            frame.destroy()
            if entry_dict in entries:
                entries.remove(entry_dict)
    
    # Add button
    Button(
        frame, 
        text=add_button_text, 
        command=add_entry,
        bg=primary_color, 
        fg="white", 
        font=default_font,
        relief="flat",
        cursor="hand2"
    ).pack(anchor="w", padx=10, pady=10)
    
    # Add first entry by default
    add_entry()
    
    return entries

# Create notebook tabs
def create_tabs():
    style = ttk.Style()
    
    # Configure the notebook background
    style.configure("TNotebook", background=secondary_color)
    
    # Configure the tabs with proper padding and font
    style.configure("TNotebook.Tab", 
                   font=heading_font, 
                   padding=[15, 5],
                   background=secondary_color,
                   foreground="#333333")
    
    # Map states to different visual styles
    # Make selected tab have white background with blue text (matching header)
    style.map("TNotebook.Tab", 
             background=[("selected", "white"), ("active", "#e6e6e6")],
             foreground=[("selected", primary_color), ("active", "#333333")])
    
    notebook = ttk.Notebook(window)
    notebook.pack(fill="both", expand=True, padx=15, pady=15)
    
    # Personal Info Tab
    personal_tab = Frame(notebook, bg=secondary_color)
    notebook.add(personal_tab, text="Personal Info")
    
    # Create a frame for better layout
    info_frame = Frame(personal_tab, bg=secondary_color)
    info_frame.pack(fill="both", expand=True, padx=10, pady=10)
    
    global entry_name, entry_email, entry_phone, entry_address, entry_linkedin, entry_website
    entry_name = create_entry_with_label(info_frame, "Name", 0, required=True)
    entry_email = create_entry_with_label(info_frame, "Email", 1, required=True)
    entry_phone = create_entry_with_label(info_frame, "Phone", 2, required=True)
    entry_address = create_entry_with_label(info_frame, "Address", 3)
    entry_linkedin = create_entry_with_label(info_frame, "LinkedIn", 4)
    entry_website = create_entry_with_label(info_frame, "Website", 5)
    
    # Education & Work Tab
    education_work_tab = Frame(notebook, bg=secondary_color)
    notebook.add(education_work_tab, text="Education & Work")
    
    # Education section (dynamic)
    global education_entries
    education_fields = {
        "Degree": {"key": "degree"},
        "Institution": {"key": "institution"},
        "Period": {"key": "period"},
        "CGPA": {"key": "cgpa"}
    }
    education_entries = create_dynamic_section(education_work_tab, "Education", education_fields, "Add Education")
    
    # Work Experience section (dynamic)
    global experience_entries
    experience_fields = {
        "Title": {"key": "title"},
        "Company": {"key": "company"},
        "Period": {"key": "period"},
        "Description": {"key": "description", "multiline": True, "height": 4},
        "Portfolio": {"key": "portfolio"}
    }
    experience_entries = create_dynamic_section(education_work_tab, "Work Experience", experience_fields, "Add Experience")
    
    # Skills & Languages Tab
    skills_tab = Frame(notebook, bg=secondary_color)
    notebook.add(skills_tab, text="Skills & Languages")
    
    # Skills sections
    skills_frame = LabelFrame(skills_tab, text="Skills Summary", font=heading_font, bg=secondary_color, fg=primary_color, bd=1, relief="solid")
    skills_frame.pack(fill="x", padx=15, pady=10)
    
    global entry_languages_skills, entry_frameworks_skills, entry_tools_skills, entry_platforms_skills
    
    skills_categories = [
        ("Languages", "entry_languages_skills"),
        ("Frameworks", "entry_frameworks_skills"),
        ("Tools", "entry_tools_skills"),
        ("Platforms", "entry_platforms_skills")
    ]
    
    for i, (label, var_name) in enumerate(skills_categories):
        frame = Frame(skills_frame, bg=secondary_color)
        frame.pack(fill="x", padx=5, pady=5)
        
        Label(frame, text=label, font=default_font, bg=secondary_color, width=12, anchor="w").pack(side=LEFT)
        entry = Entry(frame, font=default_font, bg="white", relief="solid", bd=1)
        entry.pack(side=LEFT, fill="x", expand=True, padx=(5, 0))
        globals()[var_name] = entry
    
    # Languages section
    languages_frame = LabelFrame(skills_tab, text="Languages", font=heading_font, bg=secondary_color, fg=primary_color, bd=1, relief="solid")
    languages_frame.pack(fill="x", padx=15, pady=10)
    
    global entry_languages
    entry_languages = Text(languages_frame, height=5, font=default_font, bg="white", fg="#333333", relief="solid", bd=1)
    entry_languages.pack(fill="x", expand=True, padx=10, pady=10)
    
    Label(languages_frame, text="Enter one language per line", font=("Segoe UI", 8, "italic"), bg=secondary_color).pack(padx=10)
    
    # Projects & Certifications Tab
    projects_tab = Frame(notebook, bg=secondary_color)
    notebook.add(projects_tab, text="Projects & Certs")
    
    # Projects section (dynamic)
    global project_entries
    project_fields = {
        "Name": {"key": "name"},
        "Technologies": {"key": "technologies"},
        "Description": {"key": "description", "multiline": True, "height": 4},
        "Link": {"key": "link"}
    }
    project_entries = create_dynamic_section(projects_tab, "Projects", project_fields, "Add Project")
    
    # Certifications section (dynamic)
    global certification_entries
    certification_fields = {
        "Name": {"key": "name"},
        "Issuer": {"key": "issuer"},
        "Description": {"key": "description", "multiline": True, "height": 3},
        "Skills": {"key": "skills"}
    }
    certification_entries = create_dynamic_section(projects_tab, "Certifications", certification_fields, "Add Certification")
    
    # References Tab
    references_tab = Frame(notebook, bg=secondary_color)
    notebook.add(references_tab, text="References")
    
    # References section (dynamic)
    global reference_entries
    reference_fields = {
        "Name": {"key": "name"},
        "Position": {"key": "position"},
        "Contact": {"key": "contact"},
        "Email": {"key": "email"},
        "LinkedIn": {"key": "linkedin"}
    }
    reference_entries = create_dynamic_section(references_tab, "References", reference_fields, "Add Reference")
    
    return notebook

# Create footer with generate button
def create_footer():
    footer = Frame(window, bg=secondary_color, height=60)
    footer.pack(fill="x", side="bottom")
    
    # Progress bar (hidden initially)
    progress_var = DoubleVar()
    progress = ttk.Progressbar(footer, variable=progress_var, mode="indeterminate")
    progress.pack(fill="x", padx=20, pady=(0, 10))
    progress.pack_forget()  # Hide initially
    
    # Button frame
    button_frame = Frame(footer, bg=secondary_color)
    button_frame.pack(pady=10)
    
    # Generate button with modern styling
    generate_btn = Button(
        button_frame, 
        text="Generate CV", 
        command=generate_cv_pdf, 
        bg=accent_color, 
        fg="white", 
        font=(default_font[0], default_font[1], "bold"),
        relief="flat",
        padx=20,
        pady=8,
        cursor="hand2"
    )
    generate_btn.pack()
    
    # Hover effect for button
    def on_enter(e):
        generate_btn['bg'] = '#45a049'  # Darker green on hover
    
    def on_leave(e):
        generate_btn['bg'] = accent_color
    
    generate_btn.bind("<Enter>", on_enter)
    generate_btn.bind("<Leave>", on_leave)
    
    return footer, progress, generate_btn

# Create main window
window = Tk()
window.title("Modern CV Generator")
window.geometry("800x700")
window.minsize(700, 650)

# Set app style
default_font, heading_font, primary_color, secondary_color, accent_color = set_app_style()

# Create header
header = Frame(window, bg=primary_color, height=70)
header.pack(fill="x")
Label(header, text="CV Generator", font=("Segoe UI", 18, "bold"), bg=primary_color, fg="white").pack(pady=15)

# Create tabs
notebook = create_tabs()

# Create footer with generate button
footer, progress, generate_btn = create_footer()

# Center window on screen
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")

# Run the application
window.mainloop()