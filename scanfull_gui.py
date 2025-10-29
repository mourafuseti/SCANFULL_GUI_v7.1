#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================
#   SCANFULL v7.1 - GUI com Tkinter (CORRIGIDO)
#   Criado por Leonardo de Moura Fuseti
#   Copyright 2025 - All Rights Reserved
# =============================================

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import threading
import os
import requests
from datetime import datetime
import re
import json

# PASTA DE SAÍDA
OUTPUT_DIR = "/home/kali/forcabruta"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# CORES
BG = "#1e1e1e"
FG = "#00ff00"
BTN_BG = "#333333"
BTN_FG = "#00ff00"
ENTRY_BG = "#2d2d2d"

class ScanfullGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SCANFULL v7.1 - By Leonardo de Moura Fuseti")
        self.root.geometry("1000x700")
        self.root.configure(bg=BG)
        try:
            self.root.iconbitmap("scanfull.ico")
        except:
            pass

        # Cabeçalho
        header = tk.Label(root, text="SCANFULL v7.1", font=("Courier", 20, "bold"), fg=FG, bg=BG)
        header.pack(pady=10)

        author = tk.Label(root, text="Criado por Leonardo de Moura Fuseti © 2025", font=("Arial", 10), fg="#888888", bg=BG)
        author.pack(pady=5)

        # Abas
        tab_control = ttk.Notebook(root)
        tab_control.pack(fill="both", expand=True, padx=20, pady=10)

        # === ABA 1: RECON ===
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text="Reconhecimento")

        tk.Label(tab1, text="IP ou Domínio:", fg=FG, bg=BG).pack(pady=5)
        self.entry_ip = tk.Entry(tab1, width=50, bg=ENTRY_BG, fg=FG, insertbackground=FG)
        self.entry_ip.pack(pady=5)

        btn_frame = tk.Frame(tab1, bg=BG)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Consultar IP", command=self.geo_ip, bg=BTN_BG, fg=BTN_FG).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Meu IP", command=self.my_ip, bg=BTN_BG, fg=BTN_FG).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Whois", command=self.whois, bg=BTN_BG, fg=BTN_FG).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Traceroute", command=self.traceroute, bg=BTN_BG, fg=BTN_FG).grid(row=0, column=3, padx=5)

        # === ABA 2: NMAP ===
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text="Nmap")

        tk.Label(tab2, text="Alvo (IP ou Host):", fg=FG, bg=BG).pack(pady=5)
        self.entry_nmap = tk.Entry(tab2, width=50, bg=ENTRY_BG, fg=FG, insertbackground=FG)
        self.entry_nmap.pack(pady=5)

        mode_frame = tk.Frame(tab2, bg=BG)
        mode_frame.pack(pady=10)
        self.nmap_mode = tk.StringVar(value="1")
        tk.Radiobutton(mode_frame, text="Rápido (Top 100)", variable=self.nmap_mode, value="1", fg=FG, bg=BG, selectcolor=BG).grid(row=0, column=0, padx=10)
        tk.Radiobutton(mode_frame, text="Médio (1000)", variable=self.nmap_mode, value="2", fg=FG, bg=BG, selectcolor=BG).grid(row=0, column=1, padx=10)
        tk.Radiobutton(mode_frame, text="Completo", variable=self.nmap_mode, value="3", fg=FG, bg=BG, selectcolor=BG).grid(row=0, column=2, padx=10)

        tk.Button(tab2, text="Scan Host", command=self.nmap_host, bg=BTN_BG, fg=BTN_FG, width=20).pack(pady=5)
        tk.Button(tab2, text="Scan Rede Local (/24)", command=self.nmap_network, bg=BTN_BG, fg=BTN_FG, width=20).pack(pady=5)

        # === ABA 3: WEB SCAN ===
        tab3 = ttk.Frame(tab_control)
        tab_control.add(tab3, text="Web Vulnerabilidades")

        tk.Label(tab3, text="Site ou IP:", fg=FG, bg=BG).pack(pady=5)
        self.entry_web = tk.Entry(tab3, width=50, bg=ENTRY_BG, fg=FG, insertbackground=FG)
        self.entry_web.pack(pady=5)

        tk.Button(tab3, text="Nikto Scan", command=self.nikto_scan, bg=BTN_BG, fg=BTN_FG, width=20).pack(pady=10)

        # === LOGS ===
        log_frame = tk.Frame(root, bg=BG)
        log_frame.pack(fill="both", expand=True, padx=20, pady=10)

        tk.Label(log_frame, text="Logs em Tempo Real:", fg=FG, bg=BG).pack(anchor="w")
        self.log_text = scrolledtext.ScrolledText(log_frame, height=12, bg="#000000", fg=FG, font=("Courier", 9))
        self.log_text.pack(fill="both", expand=True)

        # Rodapé
        footer = tk.Label(root, text=f"Relatórios → {OUTPUT_DIR}", fg="#888888", bg=BG, font=("Arial", 9))
        footer.pack(pady=5)

    def log(self, msg):
        self.log_text.insert(tk.END, f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")
        self.log_text.see(tk.END)

    def run_cmd(self, cmd, callback=None):
        def target():
            try:
                self.log(f"Executando: {' '.join(cmd)}")
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
                output = result.stdout + "\n" + result.stderr
                self.log(output)
                if callback:
                    callback(output)
            except Exception as e:
                self.log(f"ERRO: {e}")
        threading.Thread(target=target, daemon=True).start()

    def save_file(self, prefix, content):
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"scanfull_{prefix}_{ts}.txt"
        path = os.path.join(OUTPUT_DIR, filename)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f"SCANFULL v7.1 - {prefix.upper()}\n")
            f.write(f"Data: {datetime.now()}\n")
            f.write("="*60 + "\n")
            f.write(content)
        self.log(f"Salvo: {path}")

    def get_gateway(self):
        try:
            route = subprocess.check_output(['ip', 'route'], text=True)
            match = re.search(r'default via ([\d.]+)', route)
            return match.group(1) if match else None
        except:
            return None

    # === FUNÇÕES ===
    def geo_ip(self):
        ip = self.entry_ip.get().strip()
        if not ip:
            messagebox.showwarning("Aviso", "Digite um IP!")
            return
        self.run_cmd(["curl", "-s", f"http://ip-api.com/json/{ip}"], self.display_geo)

    def my_ip(self):
        self.run_cmd(["curl", "-s", "http://ip-api.com/json/"], self.display_geo)

    def display_geo(self, output):
        try:
            data = json.loads(output)
            if data.get("status") == "success":
                info = f"""
IP: {data['query']}
País: {data['country']} ({data['countryCode']})
Cidade: {data['city']}
ISP: {data['isp']}
Org: {data['org']}
Lat/Lon: {data['lat']}, {data['lon']}
Fuso: {data['timezone']}
                """
                self.log(info.strip())
                self.save_file(f"geo_{data['query']}", info)
            else:
                self.log(f"Erro API: {data.get('message')}")
        except Exception as e:
            self.log(f"Falha JSON: {e}")

    def whois(self):
        target = self.entry_ip.get().strip()
        if not target:
            messagebox.showwarning("Aviso", "Digite um domínio ou IP!")
            return
        self.run_cmd(["whois", target], lambda out: self.save_file(f"whois_{target}", out))

    def traceroute(self):
        target = self.entry_ip.get().strip()
        if not target:
            messagebox.showwarning("Aviso", "Digite um alvo!")
            return
        self.run_cmd(["traceroute", target], lambda out: self.save_file(f"trace_{target}", out))

    def nmap_host(self):
        target = self.entry_nmap.get().strip()
        if not target:
            messagebox.showwarning("Aviso", "Digite um IP ou Host!")
            return
        mode = self.nmap_mode.get()
        cmd = ['nmap']
        suffix = target.replace('.', '_')
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')  # DEFINIDO AQUI

        if mode == "1":
            cmd += ['-F', '--open', '-T5']
            suffix += "_fast"
        elif mode == "2":
            cmd += ['-p', '1-1000', '--open', '-T5']
            suffix += "_medium"
        else:
            cmd += ['-p-', '--open', '-sV', '-T4']
            suffix += "_full"

        xml_file = os.path.join(OUTPUT_DIR, f"scanfull_nmap_{suffix}_{ts}.xml")
        cmd += ['-oX', xml_file, target]

        self.run_cmd(cmd, lambda out: self.save_file(f"nmap_{suffix}_{ts}", out))

    def nmap_network(self):
        gateway = self.get_gateway()
        if not gateway:
            self.log("Gateway não detectado!")
            return
        network = '.'.join(gateway.split('.')[:-1]) + '.0/24'
        self.log(f"Escaneando rede: {network}")
        self.run_cmd(['nmap', '-sn', '--open', '-T4', network],
                     lambda out: self.save_file("nmap_network", out))

    def nikto_scan(self):
        target = self.entry_web.get().strip()
        if not target:
            messagebox.showwarning("Aviso", "Digite um site ou IP!")
            return
        ts = datetime.now().strftime('%Y%m%d_%H%M%S')
        safe_target = target.replace('.', '_').replace('/', '_')
        txt_file = os.path.join(OUTPUT_DIR, f"scanfull_nikto_{safe_target}_{ts}.txt")
        html_file = os.path.join(OUTPUT_DIR, f"scanfull_nikto_{safe_target}_{ts}.html")

        # Detecta portas
        self.log("Detectando portas web...")
        self.run_cmd(['nmap', '-p', '80,443,8080,8443', '--open', '-T4', target], lambda out: self.run_nikto(out, target, txt_file, html_file))

    def run_nikto(self, nmap_output, target, txt_file, html_file):
        ports = []
        for line in nmap_output.splitlines():
            if "open" in line:
                port = line.split('/')[0]
                ports.append(port)
        if not ports:
            ports = ['80', '443']

        full_output = f"SCANFULL Nikto Scan\nAlvo: {target}\nData: {datetime.now()}\nPortas: {', '.join(ports)}\n{'='*70}\n\n"
        self.log(f"Nikto em {len(ports)} porta(s): {', '.join(ports)}")

        for i, port in enumerate(ports):
            protocol = "https" if port in ['443', '8443'] else "http"
            url = f"{protocol}://{target}:{port}"
            self.log(f"Nikto → {url}")
            html_out = html_file if i == 0 else '/dev/null'
            cmd = ['nikto', '-h', url, '-output', html_out, '-Format', 'txt']
            self.run_cmd(cmd, lambda out: self.collect_nikto(out, full_output, txt_file, i == len(ports)-1))

    def collect_nikto(self, output, full_output, txt_file, is_last):
        full_output += output + "\n"
        if is_last:
            with open(txt_file, 'w', encoding='utf-8') as f:
                f.write(full_output)
            self.log(f"Relatórios salvos em: {OUTPUT_DIR}")

# === EXECUTAR ===
if __name__ == "__main__":
    root = tk.Tk()
    app = ScanfullGUI(root)
    root.mainloop()