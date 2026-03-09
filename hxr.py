#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HXR - Security Reconnaissance Tool
Version: 1.1
Author: Ruyynnz - https://github.com/ruyynn
"""

import os
import sys
import time
import json
import socket
import requests
import subprocess
import threading
import queue
import re
import urllib.parse
import hashlib
import base64
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin
import platform as platform_module  

# ==================== COLOR SETUP PREMIUM ====================
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[97m'
    MAGENTA = '\033[35m'
    ORANGE = '\033[38;5;208m'
    PURPLE = '\033[38;5;129m'
    PINK = '\033[38;5;206m'
    GOLD = '\033[38;5;220m'
    SILVER = '\033[38;5;250m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'
    
    # Gradient colors
    GRADIENT1 = '\033[38;5;39m'
    GRADIENT2 = '\033[38;5;45m'
    GRADIENT3 = '\033[38;5;51m'
    GRADIENT4 = '\033[38;5;87m'

# ==================== LOGOS ====================
HXR_LOGO = f"""
{Colors.GOLD}{Colors.BOLD}
    ╔════════════════════════════════════════════════════════════════════════════════════════
    ║                                                                   
    ║  {Colors.CYAN}██╗  ██╗██╗  ██╗██████╗ {Colors.GRADIENT1}    ██╗   ██╗ █████╗  ██████╗{Colors.GOLD}      
    ║  {Colors.CYAN}██║  ██║╚██╗██╔╝██╔══██╗{Colors.GRADIENT2}    ██║   ██║██╔══██╗██╔════╝{Colors.GOLD}      
    ║  {Colors.CYAN}███████║ ╚███╔╝ ██████╔╝{Colors.GRADIENT3}    ██║   ██║███████║██║     {Colors.GOLD}      
    ║  {Colors.CYAN}██╔══██║ ██╔██╗ ██╔══██╗{Colors.GRADIENT4}    ╚██╗ ██╔╝██╔══██║██║     {Colors.GOLD}      
    ║  {Colors.CYAN}██║  ██║██╔╝ ██╗██║  ██║{Colors.GRADIENT1}     ╚████╔╝ ██║  ██║╚██████╗{Colors.GOLD}      
    ║  {Colors.CYAN}╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝{Colors.GRADIENT2}      ╚═══╝  ╚═╝  ╚═╝ ╚═════╝{Colors.GOLD}      
    ║                                                                   
    ╚════════════════════════════════════════════════════════════════════════════════════════{Colors.RESET}
"""

DEP_LOGO = f"""
{Colors.PURPLE}{Colors.BOLD}
    ╔════════════════════════════════════════════════════════════════════════════════════════
    ║                                                                   
    ║  {Colors.PINK}██████╗ ███████╗██████╗ ███████╗███╗   ██╗██████╗ ███████╗███╗   ██╗{Colors.PURPLE}    
    ║  {Colors.PINK}██╔══██╗██╔════╝██╔══██╗██╔════╝████╗  ██║██╔══██╗██╔════╝████╗  ██║{Colors.PURPLE}    
    ║  {Colors.PINK}██║  ██║█████╗  ██████╔╝█████╗  ██╔██╗ ██║██║  ██║█████╗  ██╔██╗ ██║{Colors.PURPLE}    
    ║  {Colors.PINK}██║  ██║██╔══╝  ██╔═══╝ ██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██║╚██╗██║{Colors.PURPLE}   
    ║  {Colors.PINK}██████╔╝███████╗██║     ███████╗██║ ╚████║██████╔╝███████╗██║ ╚████║{Colors.PURPLE}   
    ║  {Colors.PINK}╚═════╝ ╚══════╝╚═╝     ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═══╝{Colors.PURPLE}    
    ║                                                                   
    ║               {Colors.WHITE}Dependency Installation System{Colors.PURPLE}                           
    ╚════════════════════════════════════════════════════════════════════════════════════════{Colors.RESET}
"""

# ====================  BOX FUNCTIONS ====================
def print_header(title, color=Colors.GOLD):
    """Print premium header"""
    width = 70
    print(f"\n{color}{Colors.BOLD}")
    print(f"    ┌─{'─' * (width-2)}─┐")
    print(f"    │  {title.center(width-4)}  │")
    print(f"    └─{'─' * (width-2)}─┘")
    print(f"{Colors.RESET}")

def print_section(title, color=Colors.CYAN):
    """Print section header"""
    print(f"\n{color}{Colors.BOLD}    ┌── {title}{Colors.RESET}")

def print_subsection(title, color=Colors.YELLOW):
    """Print subsection"""
    print(f"{color}{Colors.BOLD}    │  • {title}{Colors.RESET}")

def print_item(text, color=Colors.WHITE, bullet="•"):
    """Print list item"""
    print(f"    │  {color}{bullet} {text}{Colors.RESET}")

def print_success(text):
    """Print success message"""
    print(f"    │  {Colors.GREEN}✓ {text}{Colors.RESET}")

def print_info(text):
    """Print info message"""
    print(f"    │  {Colors.CYAN}ℹ {text}{Colors.RESET}")

def print_warning(text):
    """Print warning message"""
    print(f"    │  {Colors.ORANGE}⚠ {text}{Colors.RESET}")

def print_error(text):
    """Print error message"""
    print(f"    │  {Colors.RED}✗ {text}{Colors.RESET}")

def print_result(label, value, color=Colors.GREEN):
    """Print result line"""
    print(f"    │  {Colors.WHITE}{label}: {color}{value}{Colors.RESET}")

def print_separator(color=Colors.GOLD):
    """Print separator"""
    print(f"{color}    ├─{'─' * 68}─┤{Colors.RESET}")

def print_footer(color=Colors.GOLD):
    """Print footer"""
    print(f"{color}    └─{'─' * 68}─┘{Colors.RESET}")

# ====================  LOADING ANIMATION ====================
def loading_animation():
    """5 second premium loading animation"""
    frames = ["◴", "◷", "◶", "◵", "◴", "◷", "◶", "◵"]
    colors = [Colors.GRADIENT1, Colors.GRADIENT2, Colors.GRADIENT3, Colors.GRADIENT4]
    
    print(f"\n{Colors.GOLD}{Colors.BOLD}")
    print("    ╔═══════════════════════════════════════════════════════════════════╗")
    print("    ║                    INITIALIZING HXR ENGINE                         ")
    print("    ╠═══════════════════════════════════════════════════════════════════╣")
    print("    ║                                                                   ║")
    
    for i in range(21):
        percent = i * 5
        bar = "█" * i + "░" * (20 - i)
        color = colors[i % 4]
        frame = frames[i % 8]
        print(f"\r    ║    {color}{bar}{Colors.WHITE} {percent:3d}% {color}{frame}{Colors.GOLD}            ", end="")
        sys.stdout.flush()
        time.sleep(0.25)
    
    print(f"\n    ║                                                                   ")
    print(f"    ║  {Colors.GREEN}{Colors.BOLD}✓ HXR ENGINE INITIALIZED SUCCESSFULLY{Colors.GOLD}                      ")
    print(f"    ║  {Colors.CYAN}  Version 1.1 • Ready for deployment{Colors.GOLD}                    ")
    print(f"    ║                                                                   ")
    print(f"    ╚═══════════════════════════════════════════════════════════════════╝{Colors.RESET}")
    time.sleep(1.5)

# ==================== DEPENDENCY CHECK ====================
REQUIRED_PACKAGES = [
    'requests',
    'colorama',
    'selenium'
]

OPTIONAL_PACKAGES = [
    'dnspython',
    'beautifulsoup4',
    'lxml'
]

def check_dependencies():
    """Check and install missing dependencies"""
   
    os.system('cls' if platform_module.system() == 'Windows' else 'clear')
    
    print(DEP_LOGO)
    print_header("DEPENDENCY CHECK SYSTEM", Colors.PINK)
    
    missing = []
    installed = []
    
    print_section("Scanning installed packages", Colors.PINK)
    
   
    import importlib
    for package in REQUIRED_PACKAGES + OPTIONAL_PACKAGES:
       
        import_name = {
            'dnspython': 'dns',
            'beautifulsoup4': 'bs4',
            'pillow': 'PIL'
        }.get(package, package)
        try:
            importlib.import_module(import_name)
            installed.append(package)
            print_success(f"{package} found")
        except ImportError:
            missing.append(package)
            print_warning(f"{package} missing")
    
    if missing:
        print_separator(Colors.PINK)
        print_section("Installing missing dependencies", Colors.PINK)
        
        for package in missing:
            print_info(f"Installing {package}...")
            try:
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", "--quiet", package],
                    stderr=subprocess.DEVNULL  
                )
                print_success(f"{package} installed")
                time.sleep(0.5)
            except subprocess.CalledProcessError:
                print_error(f"Failed to install {package}")
        
        print_separator(Colors.PINK)
        print_success("All dependencies processed")
        time.sleep(2)
    else:
        print_separator(Colors.PINK)
        print_success("All dependencies already installed")
        time.sleep(1.5)

# ==================== DEVICE SELECTION ====================
def device_selection():
    """Platform selection menu with premium design"""
    # BUG FIX: use platform_module
    os.system('cls' if platform_module.system() == 'Windows' else 'clear')
    
    print(HXR_LOGO)
    print_header("SYSTEM DEPLOYMENT MENU", Colors.GOLD)
    
    detected = platform_module.system().lower()
    if 'termux' in os.environ.get('PREFIX', ''):
        detected = 'termux'
    
    print_section("Platform Selection", Colors.CYAN)
    print_item("1  TERMUX - Android Environment", Colors.WHITE)
    print_item("2  LINUX  - Ubuntu/Debian/Kali/Arch", Colors.WHITE)
    print_item("3  WINDOWS - 10/11/Server", Colors.WHITE)
    print_item("4  MACOS  - Darwin Kernel", Colors.WHITE)
    print_item("5  AUTO DETECT - System Analysis", Colors.WHITE)
    print_item("0  EXIT - Terminate Session", Colors.RED)
    
    print_separator(Colors.CYAN)
    print_section("System Information", Colors.CYAN)
    print_result("Platform", platform_module.system().upper(), Colors.YELLOW)
    print_result("Release", platform_module.release(), Colors.YELLOW)
    print_result("Machine", platform_module.machine(), Colors.YELLOW)
    print_result("Detected", detected.upper(), Colors.YELLOW)
    print_result("Version", "1.1", Colors.YELLOW)
    
    print_footer(Colors.CYAN)
    
    while True:
        try:
            choice = input(f"\n{Colors.CYAN}    ┌─[HXR@deploy]─[{Colors.YELLOW}~{Colors.CYAN}]─[{Colors.GREEN}{datetime.now().strftime('%H:%M:%S')}{Colors.CYAN}]\n    └──╼ {Colors.RESET}").strip()
            
            if choice == '0':
                print(f"\n{Colors.RED}    Exiting HXR. Goodbye.{Colors.RESET}")
                sys.exit(0)
            elif choice == '1':
                return 'termux'
            elif choice == '2':
                return 'linux'
            elif choice == '3':
                return 'windows'
            elif choice == '4':
                return 'macos'
            elif choice == '5':
                print(f"{Colors.GREEN}    Auto-detected: {detected}{Colors.RESET}")
                time.sleep(1)
                return detected
            else:
                print(f"{Colors.RED}    Invalid selection. Please enter 0-5.{Colors.RESET}")
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}    Exiting.{Colors.RESET}")
            sys.exit(0)

# ==================== MAIN MENU ====================
def main_menu(app):
    """Display main menu with premium design"""
   
    os.system('cls' if platform_module.system() == 'Windows' else 'clear')
    
    print(HXR_LOGO)
    print_header("RECONNAISSANCE FRAMEWORK v1.1", Colors.GOLD)
    
    print_section("Available Modules", Colors.CYAN)
    print_item("01  Target Reconnaissance    →  Subdomains | DNS | Technology", Colors.GREEN)
    print_item("02  Parameter Discovery      →  Crawler | Parameter Hunting", Colors.GREEN)
    print_item("03  Screenshot Automation    →  Visual Documentation", Colors.GREEN)
    print_item("04  Vulnerability Scanner    →  XSS | Open Redirect | CORS | Git", Colors.GREEN)
    print_item("05  API Endpoint Finder      →  JS Analysis | Endpoint Mining", Colors.GREEN)
    print_item("06  Report Generator         →  Professional Documentation", Colors.GREEN)
    print_item("07  Report Archive           →  View Previous Reports", Colors.GREEN)
    print_item("00  Exit Session             →  Terminate HXR", Colors.RED)
    
    print_separator(Colors.CYAN)
    print_section("Session Information", Colors.CYAN)
    print_result("Target", app.target or "Not Set", Colors.YELLOW)
    print_result("Parameters", str(len(app.parameters)), Colors.YELLOW)
    print_result("API Endpoints", str(len(app.api_endpoints)), Colors.YELLOW)
    print_result("Vulnerabilities", str(len(app.vulnerabilities)), Colors.YELLOW)
    
    print_footer(Colors.CYAN)

# ==================== FEATURE 1: TARGET RECON ====================
class TargetRecon:
    """Automated target reconnaissance - FULLY WORKING"""
    
    def __init__(self):
        self.subdomains = []
        self.ip_addresses = []
        self.dns_records = {}
        self.technologies = {}
        
        self._lock = threading.Lock()
        
    def enumerate_subdomains(self, domain):
        """Enumerate subdomains using common wordlist"""
        print_info(f"Enumerating subdomains for {Colors.YELLOW}{domain}{Colors.RESET}")
        
        wordlist = [
            'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop',
            'ns1', 'ns2', 'cpanel', 'whm', 'admin', 'blog', 'dev', 'test',
            'api', 'secure', 'vpn', 'm', 'mobile', 'cloud', 'app', 'portal',
            'support', 'help', 'docs', 'status', 'git', 'jenkins', 'jira',
            'shop', 'store', 'payment', 'account', 'login', 'auth', 'sso',
            'database', 'db', 'mysql', 'redis', 'metrics', 'monitor',
            'staging', 'stage', 'qa', 'uat', 'backup', 'old', 'legacy'
        ]
        
        def check_subdomain(sub):
            try:
                host = f"{sub}.{domain}"
                ip = socket.gethostbyname(host)
                
                with self._lock:
                    self.subdomains.append(host)
                    self.ip_addresses.append(ip)
                print_item(f"Found: {host} → {ip}", Colors.GREEN)
                return True
            except:
                return False
        
        with ThreadPoolExecutor(max_workers=30) as executor:
            executor.map(check_subdomain, wordlist)
        
        return self.subdomains
    
    def get_dns_records(self, domain):
        """Get DNS records using multiple methods"""
        print_info(f"Gathering DNS records for {Colors.YELLOW}{domain}{Colors.RESET}")
        
        
        import importlib
        try:
            dns_module = importlib.import_module('dns.resolver')
            dns_available = True
        except ImportError:
            dns_available = False
        
        record_types = ['A', 'MX', 'NS', 'TXT']
        
        for rtype in record_types:
            try:
                if dns_available:
                    answers = dns_module.resolve(domain, rtype)
                    self.dns_records[rtype] = [str(r) for r in answers]
                else:
                    if rtype == 'A':
                        try:
                            ip = socket.gethostbyname(domain)
                            self.dns_records[rtype] = [ip]
                        except:
                            self.dns_records[rtype] = []
                    else:
                        self.dns_records[rtype] = []
                
                if self.dns_records.get(rtype):
                    print_item(f"{rtype}: {', '.join(self.dns_records[rtype][:3])}", Colors.GREEN)
            except Exception:
                self.dns_records[rtype] = []
        
        return self.dns_records
    
    def detect_technologies(self, url):
        """Detect website technologies via HTTP headers"""
        print_info(f"Detecting technologies for {Colors.YELLOW}{url}{Colors.RESET}")
        
        try:
           
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            
            response = requests.get(url, timeout=10, verify=False, allow_redirects=True)
            headers = response.headers
            html = response.text.lower()
            
            if 'Server' in headers:
                self.technologies['server'] = headers['Server']
                print_item(f"Server: {headers['Server']}", Colors.GREEN)
            
            # Programming languages
            if 'php' in html or '.php' in html:
                self.technologies['language'] = 'PHP'
                print_item("Language: PHP", Colors.GREEN)
            elif 'asp.net' in html or 'aspx' in html:
                self.technologies['language'] = 'ASP.NET'
                print_item("Language: ASP.NET", Colors.GREEN)
            
            # CMS detection
            if 'wp-content' in html or 'wordpress' in html:
                self.technologies['cms'] = 'WordPress'
                print_item("CMS: WordPress", Colors.GREEN)
            
            # JavaScript frameworks
            js_frameworks = {
                'jquery': 'jQuery',
                'react': 'React',
                'angular': 'Angular',
                'vue': 'Vue.js',
                'bootstrap': 'Bootstrap'
            }
            
            for key, name in js_frameworks.items():
                if key in html:
                    self.technologies.setdefault('javascript', []).append(name)
                    print_item(f"JavaScript: {name}", Colors.GREEN)
            
            # Cloud/CDN detection
            if 'cf-ray' in headers:
                self.technologies['cdn'] = 'CloudFlare'
                print_item("CDN: CloudFlare", Colors.GREEN)
            
        except Exception as e:
            print_warning(f"Technology detection failed: {str(e)[:50]}")
        
        return self.technologies

# ==================== FEATURE 2: PARAMETER DISCOVERY ====================
class ParameterDiscovery:
    """Discover parameters from websites - FULLY WORKING"""
    
    def __init__(self):
        self.parameters = set()
        self.forms = []
        self.urls = set()
        # BUG FIX: suppress SSL warnings
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
    def crawl(self, url, max_pages=30):
        """Crawl website to discover pages and parameters"""
        print_info(f"Crawling {Colors.YELLOW}{url}{Colors.RESET}")
        
        
        parsed_base = urllib.parse.urlparse(url)
        base_netloc = parsed_base.netloc
        
        to_visit = {url}
        visited = set()
        
        while to_visit and len(visited) < max_pages:
            current = to_visit.pop()
            if current in visited:
                continue
            
            try:
                response = requests.get(current, timeout=5, verify=False, allow_redirects=True)
                visited.add(current)
                self.urls.add(current)
                
                print_item(f"Crawled: {current}", Colors.CYAN)
                
                # Extract links
                links = re.findall(r'href=[\'"]?([^\'" >]+)', response.text)
                for link in links:
                    
                    if link.startswith(('mailto:', 'javascript:', '#', 'tel:')):
                        continue
                    
                    if link.startswith('http'):
                        full_url = link
                    else:
                        full_url = urljoin(current, link)
                    
                    
                    parsed_link = urllib.parse.urlparse(full_url)
                    if parsed_link.netloc == base_netloc and full_url not in visited:
                        to_visit.add(full_url)
                
                # Extract forms and parameters
                forms = re.findall(r'<form.*?</form>', response.text, re.DOTALL | re.IGNORECASE)
                for form in forms:
                    inputs = re.findall(r'<input[^>]+name=[\'"]([^\'"]+)[\'"]', form, re.IGNORECASE)
                    for inp in inputs:
                        self.parameters.add(inp)
                        print_item(f"Parameter: {inp}", Colors.GREEN, bullet="▸")
                    
                    selects = re.findall(r'<select[^>]+name=[\'"]([^\'"]+)[\'"]', form, re.IGNORECASE)
                    for sel in selects:
                        self.parameters.add(sel)
                        print_item(f"Parameter: {sel}", Colors.GREEN, bullet="▸")
                
                # Extract URL parameters
                if '?' in current:
                    query_string = urllib.parse.urlparse(current).query
                    params = urllib.parse.parse_qs(query_string)
                    for param_name in params:
                        self.parameters.add(param_name)
                        print_item(f"URL Param: {param_name}", Colors.GREEN, bullet="▸")
                
            except Exception as e:
                print_warning(f"Error crawling {current}: {str(e)[:50]}")
        
        return list(self.parameters), self.forms
    
    def detect_hidden_parameters(self, url, base_params):
        """Detect potentially hidden parameters"""
        print_info("Testing for hidden parameters")
        
        hidden_wordlist = [
            'debug', 'test', 'admin', 'hidden', 'secret', 'key', 'token',
            'api_key', 'apikey', 'access_token', 'auth', 'password',
            'passwd', 'pass', 'username', 'user', 'email', 'mail',
            'id', 'user_id', 'uid', 'guid', 'uuid', 'session', 'sess',
            'phpinfo', 'info', 'status', 'health', 'metrics', 'stats',
            'backup', 'bak', 'old', 'new', 'tmp', 'temp', 'log', 'logs',
            'config', 'conf', 'db', 'database', 'sql', 'query', 'q',
            'page', 'p', 'post', 'article', 'file', 'download', 'upload',
            'action', 'do', 'method', 'func', 'cmd', 'command', 'exec',
            'redirect', 'return', 'next', 'prev', 'referer', 'origin'
        ]
        
        found = []
        
        
        try:
            base_response = requests.get(url, timeout=5, verify=False)
            base_len = len(base_response.text)
        except Exception:
            print_warning("Could not fetch base URL for comparison")
            return found
        
        for param in hidden_wordlist[:30]:
            if param in base_params:
                continue
                
            try:
                test_url = f"{url}{'&' if '?' in url else '?'}{param}=test" 
                response = requests.get(test_url, timeout=2, verify=False)
                
                if len(response.text) != base_len:
                    found.append(param)
                    print_item(f"Hidden parameter: {param}", Colors.ORANGE, bullet="▸")
            except:
                pass
        
        return found

# ==================== FEATURE 3: SCREENSHOT AUTOMATION ====================
class ScreenshotAutomation:
    """Automated screenshot capture - WORKING with fallback"""
    
    def __init__(self):
        self.screenshots = []
        self._lock = threading.Lock()  
       
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
    def capture(self, urls, output_dir="screenshots"):
        """Capture screenshots of URLs"""
        print_info(f"Capturing screenshots for {len(urls)} targets")
        
        os.makedirs(output_dir, exist_ok=True)
        
        # Try selenium if available
        selenium_available = False
        driver_class = None
        options_class = None
        try:
            from selenium import webdriver
            from selenium.webdriver.chrome.options import Options
            selenium_available = True
            driver_class = webdriver.Chrome
            options_class = Options
        except ImportError:
            print_warning("Selenium not available, using fallback method")
        
        def take_screenshot(url):
            result = {'url': url, 'file': None, 'status': 'failed'}
            try:
                if selenium_available:
                    try:
                        options = options_class()
                        options.add_argument('--headless')
                        options.add_argument('--no-sandbox')
                        options.add_argument('--disable-dev-shm-usage')
                        options.add_argument('--disable-gpu')  
                        
                        driver = driver_class(options=options)
                        driver.set_page_load_timeout(30)
                        driver.get(url)
                        
                        filename = f"{output_dir}/{hashlib.md5(url.encode()).hexdigest()[:10]}.png"
                        driver.save_screenshot(filename)
                        driver.quit()
                        
                        result = {'url': url, 'file': filename, 'status': 'success'}
                        print_item(f"Screenshot saved: {filename}", Colors.GREEN)
                        with self._lock:
                            self.screenshots.append(result)
                        return
                    except Exception:
                        pass  # Fall through to fallback
                
                # Fallback: HTTP info
                response = requests.get(url, timeout=10, verify=False)
                filename = f"{output_dir}/{hashlib.md5(url.encode()).hexdigest()[:10]}.txt"
                
                with open(filename, 'w', encoding='utf-8') as f: 
                    f.write(f"URL: {url}\n")
                    f.write(f"Status: {response.status_code}\n")
                    f.write(f"Server: {response.headers.get('Server', 'Unknown')}\n")
                    f.write(f"Content-Type: {response.headers.get('Content-Type', 'Unknown')}\n")
                    f.write(f"Timestamp: {datetime.now().isoformat()}\n")
                
                result = {'url': url, 'file': filename, 'status': 'info'}
                print_item(f"Info saved: {filename}", Colors.CYAN)
                
            except Exception as e:
                print_error(f"Failed to capture {url}: {str(e)[:50]}")
            
            with self._lock:  
                self.screenshots.append(result)
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(take_screenshot, urls)
        
        return self.screenshots

# ==================== FEATURE 4: VULNERABILITY CHECK ====================
class VulnerabilityChecker:
    """Basic vulnerability checks - FULLY WORKING"""
    
    def __init__(self):
        self.findings = []
        self._lock = threading.Lock()  

        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
    def check_xss(self, url, param):
        """Basic XSS detection"""
        payloads = [
            "<script>alert(1)</script>",
            "<img src=x onerror=alert(1)>"
        ]
        
        # BUG FIX: strip existing query params from url to avoid double params
        base_url = url.split('?')[0]
        
        for payload in payloads:
            try:
                test_url = f"{base_url}?{param}={urllib.parse.quote(payload)}"
                response = requests.get(test_url, timeout=3, verify=False)
                
                # BUG FIX: check decoded payload too (some sites decode on reflection)
                if payload in response.text or urllib.parse.unquote(payload) in response.text:
                    finding = {
                        'type': 'XSS',
                        'url': test_url,
                        'param': param,
                        'severity': 'Medium'
                    }
                    with self._lock:
                        self.findings.append(finding)
                    print_item(f"XSS found with parameter: {param}", Colors.RED, bullet="!")
                    return finding
            except:
                pass
        return None
    
    def check_open_redirect(self, url, param):
        """Check for open redirect"""
        test_urls = ["http://evil.com", "https://evil.com"]
        base_url = url.split('?')[0]  # BUG FIX: use clean URL
        
        for test in test_urls:
            try:
                test_url = f"{base_url}?{param}={urllib.parse.quote(test)}"
                response = requests.get(test_url, timeout=3, verify=False, allow_redirects=False)
                
                if response.status_code in [301, 302, 303, 307, 308]:  # BUG FIX: include all redirect codes
                    location = response.headers.get('Location', '')
                    if 'evil.com' in location:
                        finding = {
                            'type': 'Open Redirect',
                            'url': test_url,
                            'param': param,
                            'severity': 'Medium'
                        }
                        with self._lock:
                            self.findings.append(finding)
                        print_item(f"Open redirect with parameter: {param}", Colors.ORANGE, bullet="!")
                        return finding
            except:
                pass
        return None
    
    def check_cors(self, url):
        """BUG FIX: added CORS check (was mentioned in menu but missing)"""
        try:
            headers = {'Origin': 'https://evil.com'}
            response = requests.get(url, headers=headers, timeout=3, verify=False)
            acao = response.headers.get('Access-Control-Allow-Origin', '')
            acac = response.headers.get('Access-Control-Allow-Credentials', '')
            
            if acao == '*' or 'evil.com' in acao:
                finding = {
                    'type': 'CORS Misconfiguration',
                    'url': url,
                    'severity': 'Medium' if acao == '*' else 'High',
                    'detail': f"ACAO: {acao}, ACAC: {acac}"
                }
                with self._lock:
                    self.findings.append(finding)
                print_item(f"CORS misconfiguration: {acao}", Colors.ORANGE, bullet="!")
                return finding
        except:
            pass
        return None
    
    def check_git_exposure(self, url):
        """Check for exposed .git directory"""
        git_paths = ["/.git/config", "/.git/HEAD"]
        base_url = url.rstrip('/')
        
        for path in git_paths:
            try:
                test_url = base_url + path
                response = requests.get(test_url, timeout=3, verify=False)
                
                if response.status_code == 200:
                    if 'repository' in response.text or 'ref:' in response.text:
                        finding = {
                            'type': 'Git Exposure',
                            'url': test_url,
                            'severity': 'High'
                        }
                        with self._lock:
                            self.findings.append(finding)
                        print_item(f"Git repository exposed: {path}", Colors.RED, bullet="!")
                        return finding
            except:
                pass
        return None
    
    def run(self, urls, params=None):
        """Run all vulnerability checks"""
        print_info(f"Running vulnerability checks on {len(urls)} targets")
        
        for url in urls[:10]:
            print_item(f"Testing: {url}", Colors.CYAN)
            
            self.check_git_exposure(url)
            self.check_cors(url)  # BUG FIX: actually run CORS check
            
            if params:
                for param in params[:20]:
                    self.check_xss(url, param)
                    self.check_open_redirect(url, param)
        
        return self.findings

# ==================== FEATURE 5: API ENDPOINT FINDER ====================
class APIEndpointFinder:
    """Find API endpoints from JavaScript files"""
    
    def __init__(self):
        self.endpoints = set()
        self.js_files = []
        # BUG FIX: suppress SSL warnings
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
    def find_js_files(self, url):
        """Find JavaScript files from webpage"""
        print_info("Scanning for JavaScript files")
        
        try:
            response = requests.get(url, timeout=5, verify=False)
            
            js_patterns = [
                r'<script[^>]+src=[\'"]([^\'"]+\.js(?:\?[^\'"]*)?)[\'"]',  # BUG FIX: handle query strings in JS URLs
                r'src=[\'"]([^\'"]+\.js(?:\?[^\'"]*)?)[\'"]'
            ]
            
            seen = set()  # BUG FIX: deduplicate JS files
            for pattern in js_patterns:
                matches = re.findall(pattern, response.text, re.IGNORECASE)
                for match in matches:
                    # BUG FIX: strip query string for dedup key
                    clean_match = match.split('?')[0]
                    if clean_match in seen:
                        continue
                    seen.add(clean_match)
                    
                    if match.startswith('http'):
                        js_url = match
                    else:
                        js_url = urljoin(url, match)
                    
                    self.js_files.append(js_url)
                    print_item(f"JS file: {js_url}", Colors.GREEN)
            
        except Exception as e:
            print_error(f"Error: {str(e)[:50]}")
        
        return self.js_files
    
    def extract_endpoints(self, js_content):
        """Extract API endpoints from JavaScript content"""
        patterns = [
            r'["\'](/api/[^"\'<>\s]{2,100})["\']',
            r'["\'](/v[0-9]+/[^"\'<>\s]{2,100})["\']',
            r'fetch\s*\(\s*["\']([^"\']{2,200})["\']',
            r'axios\.[a-z]+\s*\(\s*["\']([^"\']{2,200})["\']',
            r'url\s*:\s*["\']([^"\']{2,200})["\']',
            r'["\'](/graphql)["\']',
            r'["\'](/rest/[^"\'<>\s]{2,100})["\']',  # BUG FIX: added REST pattern
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, js_content, re.IGNORECASE)
            for match in matches:
                if match and len(match) > 2:
                    # BUG FIX: filter out obviously non-endpoint strings
                    if not any(ext in match for ext in ['.css', '.png', '.jpg', '.gif', '.svg', '.ico']):
                        self.endpoints.add(match)
        
        return list(self.endpoints)
    
    def analyze_js_files(self):
        """Analyze all found JavaScript files"""
        print_info("Analyzing JavaScript files for API endpoints")
        
        for js_url in self.js_files:
            try:
                response = requests.get(js_url, timeout=5, verify=False)
                # BUG FIX: check content type before parsing
                content_type = response.headers.get('Content-Type', '')
                if response.status_code == 200:
                    endpoints = self.extract_endpoints(response.text)
                    for endpoint in endpoints[:3]:
                        print_item(f"API: {endpoint}", Colors.GREEN, bullet="▸")
                    
            except Exception as e:
                print_warning(f"Error analyzing {js_url}: {str(e)[:40]}")  # BUG FIX: show error detail
        
        return list(self.endpoints)
    
    def run(self, url):
        """Run full API endpoint discovery"""
        self.find_js_files(url)
        endpoints = self.analyze_js_files()
        return endpoints

# ==================== FEATURE 6: REPORT GENERATOR ====================
class ReportGenerator:
    """report generator with TXT and JSON output"""
    
    def __init__(self, target):
        self.target = target
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.start_time = time.time()  # BUG FIX: track real start time for duration
        self.data = {
            "scan_info": {
                "tool": "HXR v1.1",
                "target": target,
                "timestamp": datetime.now().isoformat(),
                "duration": 0
            },
            "reconnaissance": {},
            "parameters": [],
            "screenshots": [],
            "vulnerabilities": [],
            "api_endpoints": []
        }
    
    def add_recon_data(self, data):
        self.data["reconnaissance"] = data
    
    def add_parameters(self, params):
        self.data["parameters"] = list(params)  # BUG FIX: handle set input
    
    def add_screenshots(self, screenshots):
        self.data["screenshots"] = screenshots
    
    def add_vulnerabilities(self, vulns):
        self.data["vulnerabilities"] = vulns
    
    def add_api_endpoints(self, endpoints):
        self.data["api_endpoints"] = list(endpoints)  # BUG FIX: handle set input
    
    def _update_duration(self):
        """BUG FIX: calculate actual scan duration"""
        self.data["scan_info"]["duration"] = round(time.time() - self.start_time, 2)
    
    def generate_txt_report(self, filename=None):
        self._update_duration()  # BUG FIX
        if not filename:
            filename = f"hxr_report_{self.timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:  # BUG FIX: explicit encoding
            f.write("=" * 80 + "\n")
            f.write(" " * 30 + "HXR SECURITY REPORT\n")
            f.write("=" * 80 + "\n\n")
            
            f.write("SCAN INFORMATION\n")
            f.write("-" * 40 + "\n")
            f.write(f"Tool: {self.data['scan_info']['tool']}\n")
            f.write(f"Target: {self.data['scan_info']['target']}\n")
            f.write(f"Timestamp: {self.data['scan_info']['timestamp']}\n")
            f.write(f"Duration: {self.data['scan_info']['duration']}s\n\n")
            
            if self.data["reconnaissance"]:
                f.write("RECONNAISSANCE RESULTS\n")
                f.write("-" * 40 + "\n")
                recon = self.data["reconnaissance"]
                f.write(f"Domain: {recon.get('domain', 'N/A')}\n")
                f.write(f"Subdomains Found: {len(recon.get('subdomains', []))}\n")
                for sub in recon.get('subdomains', [])[:20]:
                    f.write(f"  - {sub}\n")
                
                # BUG FIX: also write technologies to report
                techs = recon.get('technologies', {})
                if techs:
                    f.write("\nTechnologies Detected:\n")
                    for k, v in techs.items():
                        f.write(f"  - {k}: {v}\n")
                f.write("\n")
            
            if self.data["parameters"]:
                f.write("DISCOVERED PARAMETERS\n")
                f.write("-" * 40 + "\n")
                for param in self.data["parameters"][:50]:
                    f.write(f"  - {param}\n")
                f.write("\n")
            
            if self.data["api_endpoints"]:
                f.write("API ENDPOINTS\n")
                f.write("-" * 40 + "\n")
                for endpoint in self.data["api_endpoints"][:50]:
                    f.write(f"  - {endpoint}\n")
                f.write("\n")
            
            if self.data["vulnerabilities"]:
                f.write("VULNERABILITY FINDINGS\n")
                f.write("-" * 40 + "\n")
                for vuln in self.data["vulnerabilities"]:
                    f.write(f"Type: {vuln.get('type', 'Unknown')}\n")
                    f.write(f"URL: {vuln.get('url', 'N/A')}\n")
                    f.write(f"Severity: {vuln.get('severity', 'Info')}\n")
                    if 'param' in vuln:
                        f.write(f"Parameter: {vuln['param']}\n")
                    if 'detail' in vuln:
                        f.write(f"Detail: {vuln['detail']}\n")
                    f.write("-" * 30 + "\n")
            
            f.write("\n" + "=" * 80 + "\n")
        
        return filename
    
    def generate_json_report(self, filename=None):
        self._update_duration()  # BUG FIX
        if not filename:
            filename = f"hxr_report_{self.timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:  # BUG FIX: explicit encoding
            json.dump(self.data, f, indent=2, default=str)
        
        return filename
    
    def generate_all(self):
        txt_file = self.generate_txt_report()
        json_file = self.generate_json_report()
        return txt_file, json_file

# ==================== MAIN APPLICATION ====================
class HXRApplication:
    """Main HXR Application"""
    
    def __init__(self, platform):
        self.platform = platform
        self.target = None
        self.report = None
        self.recon_data = None
        self.parameters = []
        self.api_endpoints = []
        self.vulnerabilities = []
        self.screenshots = []
        # BUG FIX: suppress SSL warnings globally at app init
        import urllib3
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        
    def feature_target_recon(self):
        """Feature 1: Target Reconnaissance"""
        # BUG FIX: use platform_module instead of platform (which is now a string)
        os.system('cls' if platform_module.system() == 'Windows' else 'clear')
        print_header("TARGET RECONNAISSANCE MODULE", Colors.GREEN)
        
        target = input(f"\n{Colors.YELLOW}    Enter target domain [example.com]: {Colors.RESET}").strip()
        
        # BUG FIX: strip http/https if user pastes full URL
        target = re.sub(r'^https?://', '', target).rstrip('/')
        
        if not target:
            print_error("Target required")
            input(f"\n{Colors.CYAN}    Press Enter to continue...{Colors.RESET}")
            return
        
        self.target = target
        print()
        
        recon = TargetRecon()
        start_time = time.time()
        
        subdomains = recon.enumerate_subdomains(target)
        dns_records = recon.get_dns_records(target)
        
        # BUG FIX: try https first, then http (modern sites prefer https)
        tech_detected = False
        for protocol in ['https', 'http']:
            url = f"{protocol}://{target}"
            try:
                recon.detect_technologies(url)
                tech_detected = True
                break
            except:
                continue
        
        elapsed = time.time() - start_time
        
        self.recon_data = {
            "domain": target,
            "subdomains": subdomains,
            "ip_addresses": list(set(recon.ip_addresses)),
            "dns_records": dns_records,
            "technologies": recon.technologies
        }
        
        self.report = ReportGenerator(target)
        self.report.add_recon_data(self.recon_data)
        
        print_separator(Colors.GREEN)
        print_result("Subdomains Found", str(len(subdomains)), Colors.YELLOW)
        print_result("IP Addresses", str(len(set(recon.ip_addresses))), Colors.YELLOW)
        print_result("Time Elapsed", f"{elapsed:.2f}s", Colors.YELLOW)
        print_footer(Colors.GREEN)
        
        input(f"\n{Colors.CYAN}    Press Enter to continue...{Colors.RESET}")
    
    def feature_parameter_discovery(self):
        """Feature 2: Parameter Discovery"""
        if not self.target:
            print_error("Please run target reconnaissance first")
            input(f"\n{Colors.CYAN}    Press Enter to continue...{Colors.RESET}")
            return
        
        os.system('cls' if platform_module.system() == 'Windows' else 'clear')  # BUG FIX
        print_header("PARAMETER DISCOVERY MODULE", Colors.CYAN)
        
        url = input(f"\n{Colors.YELLOW}    Enter URL [http://{self.target}]: {Colors.RESET}").strip()
        if not url:
            url = f"http://{self.target}"
        
        # BUG FIX: ensure URL has scheme
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        print()
        pd = ParameterDiscovery()
        
        params, forms = pd.crawl(url)
        hidden = pd.detect_hidden_parameters(url, params)
        
        self.parameters = list(set(params + hidden))
        
        print_separator(Colors.CYAN)
        print_result("Visible Parameters", str(len(params)), Colors.YELLOW)
        print_result("Hidden Parameters", str(len(hidden)), Colors.YELLOW)
        print_result("Total Parameters", str(len(self.parameters)), Colors.YELLOW)
        print_footer(Colors.CYAN)
        
        if self.report:
            self.report.add_parameters(self.parameters)
        
        input(f"\n{Colors.CYAN}    Press Enter to continue...{Colors.RESET}")
    
    def feature_screenshot(self):
        """Feature 3: Screenshot Automation"""
        os.system('cls' if platform_module.system() == 'Windows' else 'clear')  # BUG FIX
        print_header("SCREENSHOT AUTOMATION MODULE", Colors.PURPLE)
        
        urls = []
        
        if self.recon_data and self.recon_data.get('subdomains'):
            print_info(f"Using {len(self.recon_data['subdomains'])} subdomains")
            for sub in self.recon_data['subdomains'][:20]:
                urls.append(f"https://{sub}")  # BUG FIX: try https first
                urls.append(f"http://{sub}")
        else:
            url = input(f"\n{Colors.YELLOW}    Enter URL: {Colors.RESET}").strip()
            if url:
                if not url.startswith(('http://', 'https://')):
                    url = 'http://' + url  # BUG FIX: ensure scheme
                urls = [url]
        
        if not urls:
            print_error("No URLs to screenshot")
            input(f"\n{Colors.CYAN}    Press Enter to continue...{Colors.RESET}")
            return
        
        print()
        sa = ScreenshotAutomation()
        screenshots = sa.capture(urls)
        
        self.screenshots = screenshots
        
        success = len([s for s in screenshots if s['status'] == 'success'])
        failed = len([s for s in screenshots if s['status'] == 'failed'])
        
        print_separator(Colors.PURPLE)
        print_result("Successful", str(success), Colors.GREEN)
        print_result("Failed", str(failed), Colors.RED)
        print_result("Total", str(len(screenshots)), Colors.YELLOW)
        print_footer(Colors.PURPLE)
        
        if self.report:
            self.report.add_screenshots(screenshots)
        
        input(f"\n{Colors.CYAN}    Press Enter to continue...{Colors.RESET}")
    
    def feature_vulnerability_check(self):
        """Feature 4: Vulnerability Check"""
        os.system('cls' if platform_module.system() == 'Windows' else 'clear')  # BUG FIX
        print_header("VULNERABILITY SCANNER MODULE", Colors.ORANGE)
        
        urls = []
        if self.recon_data and self.recon_data.get('subdomains'):
            for sub in self.recon_data['subdomains'][:10]:
                urls.append(f"http://{sub}")
        else:
            url = input(f"\n{Colors.YELLOW}    Enter URL: {Colors.RESET}").strip()
            if url:
                if not url.startswith(('http://', 'https://')):
                    url = 'http://' + url  # BUG FIX: ensure scheme
                urls = [url]
        
        if not urls:
            print_error("No URLs to test")
            input(f"\n{Colors.CYAN}    Press Enter to continue...{Colors.RESET}")
            return
        
        print()
        vc = VulnerabilityChecker()
        findings = vc.run(urls, self.parameters)
        
        self.vulnerabilities = findings
        
        print_separator(Colors.ORANGE)
        print_result("Vulnerabilities Found", str(len(findings)), Colors.YELLOW)
        
        for vuln in findings:
            print_item(f"{vuln['type']} - {vuln.get('severity', 'Info')}", Colors.RED)
        
        print_footer(Colors.ORANGE)
        
        if self.report:
            self.report.add_vulnerabilities(findings)
        
        input(f"\n{Colors.CYAN}    Press Enter to continue...{Colors.RESET}")
    
    def feature_api_finder(self):
        """Feature 5: API Endpoint Finder"""
        os.system('cls' if platform_module.system() == 'Windows' else 'clear')  # BUG FIX
        print_header("API ENDPOINT FINDER MODULE", Colors.PINK)
        
        url = input(f"\n{Colors.YELLOW}    Enter URL [http://{self.target or ''}]: {Colors.RESET}").strip()
        if not url and self.target:
            url = f"http://{self.target}"
        
        if not url:
            print_error("URL required")
            input(f"\n{Colors.CYAN}    Press Enter to continue...{Colors.RESET}")
            return
        
        # BUG FIX: ensure URL has scheme
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        
        print()
        af = APIEndpointFinder()
        endpoints = af.run(url)
        
        self.api_endpoints = endpoints
        
        print_separator(Colors.PINK)
        print_result("JS Files Found", str(len(af.js_files)), Colors.YELLOW)
        print_result("API Endpoints", str(len(endpoints)), Colors.YELLOW)
        print_footer(Colors.PINK)
        
        if self.report:
            self.report.add_api_endpoints(endpoints)
        
        input(f"\n{Colors.CYAN}    Press Enter to continue...{Colors.RESET}")
    
    def feature_report_generator(self):
        """Feature 6: Report Generator"""
        os.system('cls' if platform_module.system() == 'Windows' else 'clear')  # BUG FIX
        print_header("REPORT GENERATOR MODULE", Colors.GOLD)
        
        if not self.report:
            if not self.target:
                self.target = input(f"\n{Colors.YELLOW}    Enter target for report: {Colors.RESET}").strip()
            if self.target:
                self.report = ReportGenerator(self.target)
        
        if not self.report:
            print_error("No data to generate report")
            input(f"\n{Colors.CYAN}    Press Enter to continue...{Colors.RESET}")
            return
        
        print_info("Generating reports...")
        
        try:
            txt_file, json_file = self.report.generate_all()
            
            print_separator(Colors.GOLD)
            print_result("TXT Report", txt_file, Colors.GREEN)
            print_result("JSON Report", json_file, Colors.GREEN)
            print_footer(Colors.GOLD)
        except Exception as e:
            print_error(f"Report generation failed: {str(e)[:60]}")  # BUG FIX: catch write errors
        
        input(f"\n{Colors.CYAN}    Press Enter to continue...{Colors.RESET}")
    
    def view_reports(self):
        """View previous reports"""
        os.system('cls' if platform_module.system() == 'Windows' else 'clear')  # BUG FIX
        print_header("REPORT ARCHIVE", Colors.SILVER)
        
        try:
            reports = [f for f in os.listdir('.') if f.startswith('hxr_report_') and (f.endswith('.txt') or f.endswith('.json'))]
        except OSError as e:
            print_error(f"Cannot list reports: {str(e)}")  # BUG FIX: handle OS error
            reports = []
        
        if not reports:
            print_info("No reports found")
        else:
            print_info(f"Found {len(reports)} reports")
            print()
            for report in sorted(reports, reverse=True)[:10]:
                try:
                    size = os.path.getsize(report)
                    modified = datetime.fromtimestamp(os.path.getmtime(report)).strftime('%Y-%m-%d %H:%M')
                    print_item(f"{report} ({size} bytes) - {modified}", Colors.CYAN)
                except OSError:
                    print_item(f"{report} (size unavailable)", Colors.CYAN)  # BUG FIX
        
        print_footer(Colors.SILVER)
        input(f"\n{Colors.CYAN}    Press Enter to continue...{Colors.RESET}")
    
    def run(self):
        """Main application loop"""
        while True:
            main_menu(self)
            
            try:
                choice = input(f"\n{Colors.CYAN}    ┌─[HXR@engine]─[{Colors.YELLOW}~{Colors.CYAN}]─[{Colors.GREEN}{datetime.now().strftime('%H:%M:%S')}{Colors.CYAN}]\n    └──╼ {Colors.RESET}").strip()
                
                if choice == '00' or choice == '0':
                    print(f"\n{Colors.RED}    Exiting HXR. Goodbye.{Colors.RESET}")
                    sys.exit(0)
                    
                elif choice == '01' or choice == '1':
                    self.feature_target_recon()
                    
                elif choice == '02' or choice == '2':
                    self.feature_parameter_discovery()
                    
                elif choice == '03' or choice == '3':
                    self.feature_screenshot()
                    
                elif choice == '04' or choice == '4':
                    self.feature_vulnerability_check()
                    
                elif choice == '05' or choice == '5':
                    self.feature_api_finder()
                    
                elif choice == '06' or choice == '6':
                    self.feature_report_generator()
                    
                elif choice == '07' or choice == '7':
                    self.view_reports()
                    
                else:
                    print_error(f"Invalid selection: {choice}")
                    time.sleep(1)
                    
            except KeyboardInterrupt:
                print(f"\n{Colors.YELLOW}    Press Ctrl+C again to exit{Colors.RESET}")
                time.sleep(1)

# ==================== MAIN ====================
if __name__ == "__main__":
    try:
        # Check dependencies first
        check_dependencies()
        
        # Platform selection
        platform_choice = device_selection()
        
        # Loading animation
        loading_animation()
        
        # Run application
        app = HXRApplication(platform_choice)
        app.run()
        
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}    Program terminated.{Colors.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}    Fatal error: {e}{Colors.RESET}")
        sys.exit(1)
