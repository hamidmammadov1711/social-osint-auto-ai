import sys
import os
import platform
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.align import Align
from rich.text import Text

# Add src to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.utils.logger import logger, console
from src.core.anonymity import anonymity
from src.modules.social import social_search
from src.modules.email_checker import email_checker
from src.modules.ip_intelligence import ip_intel
from src.reports.engine import report_engine
from src.utils.i18n import i18n

def display_banner():
    # Modern Cybersecurity Banner
    banner_text = Text()
    banner_text.append(" ██████╗ ███████╗██╗███╗   ██╗████████╗    ██████╗ ██╗   ██╗\n", style="bold green")
    banner_text.append("██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝    ██╔══██╗╚██╗ ██╔╝\n", style="bold green")
    banner_text.append("██║   ██║███████╗██║██╔██╗ ██║   ██║       ██████╔╝ ╚████╔╝ \n", style="bold green")
    banner_text.append("██║   ██║╚════██║██║██║╚██╗██║   ██║       ██╔══██╗  ╚██╔╝  \n", style="bold green")
    banner_text.append("╚██████╔╝███████║██║██║ ╚████║   ██║       ██████╔╝   ██║   \n", style="bold green")
    banner_text.append(" ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝       ╚═════╝    ╚═╝   \n", style="bold green")
    banner_text.append("\n[ G O V E R N M E N T   G R A D E   O S I N T   S Y S T E M ]\n", style="bold white blink")
    banner_text.append("------------------------------------------------------------\n", style="dim green")
    banner_text.append(f"Author: Hamid Mammadov | Version: 3.5 (Hacker Edition)\n", style="dim cyan")
    banner_text.append(f"OS Detected: {platform.system()} {platform.release()}\n", style="dim yellow")
    
    panel = Panel(Align.center(banner_text), style="bold green", border_style="green", padding=(1, 2))
    console.print(panel)

def select_language():
    choice = Prompt.ask("[?] Dil seçin / Select Language", choices=["1", "2"], default="1")
    if choice == "2":
        i18n.lang = "EN"
        from src.utils.i18n import Translation
        i18n.strings = Translation.EN
    else:
        i18n.lang = "AZ"
        from src.utils.i18n import Translation
        i18n.strings = Translation.AZ

def main_menu():
    display_banner()
    
    table = Table(title=i18n.get("menu_title"), show_header=True, header_style="bold green", box=None)
    table.add_column("CODE", justify="center", style="bold green")
    table.add_column("MODULE", style="bold white")
    
    table.add_row("01", i18n.get("opt_1"))
    table.add_row("02", i18n.get("opt_2"))
    table.add_row("03", i18n.get("opt_3"))
    table.add_row("04", i18n.get("opt_4"))
    table.add_row("05", i18n.get("opt_5"))
    table.add_row("06", i18n.get("opt_6"))
    
    console.print(Align.center(table))
    
    choice = Prompt.ask(f"\n[root@osint] # ", choices=["1", "2", "3", "4", "5", "6"], default="4")
    return choice

def run_full_scan(target_info):
    results = {}
    target_name = target_info.get("username") or target_info.get("email") or target_info.get("ip") or "unknown"
    
    console.print(f"\n[bold green][*] Initiating Cyber Reconnaissance on: {target_name}[/bold green]")
    
    with Progress(
        SpinnerColumn(spinner_name="dots12"),
        TextColumn("[bold green]{task.description}"),
        BarColumn(bar_width=40, style="dim green", complete_style="green"),
        transient=True,
    ) as progress:
        
        if target_info.get("username"):
            task = progress.add_task(description=f"  > Scanning Social Grid: {target_info['username']}", total=100)
            results["social"] = social_search.search_username(target_info["username"])
            progress.update(task, completed=100)
            
        if target_info.get("email"):
            task = progress.add_task(description=f"  > Breached Database Lookup: {target_info['email']}", total=100)
            results["email"] = email_checker.check(target_info["email"])
            progress.update(task, completed=100)
            
        if target_info.get("ip"):
            task = progress.add_task(description=f"  > Signal Geolocation: {target_info['ip']}", total=100)
            results["ip_intel"] = ip_intel.analyze(target_info["ip"])
            progress.update(task, completed=100)
            
    # Generate reports
    report_path = report_engine.generate(results, target_name)
    
    console.print(f"\n[bold green][✓] {i18n.get('scan_complete')}[/bold green]")
    console.print(Panel(f"ACCESS SECURED: {report_path}", style="bold green", border_style="green"))

if __name__ == "__main__":
    try:
        select_language()
        while True:
            choice = main_menu()
            
            if choice == "1":
                username = Prompt.ask(f"[?] {i18n.get('target')} Username")
                run_full_scan({"username": username})
                
            elif choice == "2":
                email = Prompt.ask(f"[?] {i18n.get('target')} Email")
                run_full_scan({"email": email})
                
            elif choice == "3":
                ip = Prompt.ask(f"[?] {i18n.get('target')} IP/Domain")
                run_full_scan({"ip": ip})
                
            elif choice == "4":
                username = Prompt.ask(f"[?] Username (optional)", default="")
                email = Prompt.ask(f"[?] Email (optional)", default="")
                ip = Prompt.ask(f"[?] IP/Domain (optional)", default="")
                run_full_scan({"username": username, "email": email, "ip": ip})
                
            elif choice == "5":
                console.print(f"[bold yellow][!] {i18n.get('anonymous_msg')}[/bold yellow]")
                anonymity.change_mac()
                anonymity.setup_tor()
                Prompt.ask("\n[ENTER to continue]")
                
            elif choice == "6":
                console.print("[bold red]Session Terminated.[/bold red]")
                break
                
    except KeyboardInterrupt:
        console.print("\n[bold red][!] Emergency Shutdown Initiated.[/bold red]")
        sys.exit(0)
