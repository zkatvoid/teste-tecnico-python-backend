# Desafio Backend

Pra rodar, precisa do `uv`:
https://docs.astral.sh/uv/

Entre na pasta do projeto

Rode na sequencia
`cd python` -> Entra na pasta do django
`uv venv --python 3.14` -> Cria a venv
`source .venv/bin/activate` -> Ativa a venv
`uv sync` -> Instala dependencias
`python manage.py migrate` -> Cria db (sqlite3)
`python manage.py runserver` -> API rodando no http://localhost:8000

Opcional:
Se quiser ver os registros na tela de admin, rode:
`python manage.py createsuperuser` -> Segue o passo a passo e cria um superuser

Navegue ate http://localhost:8000/admin e faca login com o usuario/senha que acabou de criar


---

Desafio feito 100% sem uso de nenhuma IA em um sistema totalmente cru e recem instalado:

Sistema:
z@z
OS: Void Linux x86_64
Host: KVM/QEMU Standard PC (Q35 + ICH9, 2009) (pc-q35-10.2)
Kernel: Linux 6.18.26_1
Uptime: 45 mins
Packages: 664 (xbps)
Shell: bash 5.3.0
Display (Virtual-1): 1600x900, 60 Hz
DE: Xfce4 4.20
WM: Xfwm4 (X11)
WM Theme: Default
Theme: Adwaita [GTK2/3/4]
Icons: Adwaita [GTK2/3/4]
Font: Sans (10pt) [GTK2/3/4]
Terminal: tmux 3.6a
CPU: 6 x AMD Ryzen 5 7600 (6) @ 3.80 GHz
GPU: Red Hat, Inc. QXL paravirtual graphic card
Memory: 2.47 GiB / 7.76 GiB (32%)
Swap: Disabled
Disk (/): 7.34 GiB / 29.36 GiB (25%) - ext4
Local IP (eth0): 192.168.1.178/24
Locale: en_US.UTF-8

E-mail: zkdevoid@proton.me
