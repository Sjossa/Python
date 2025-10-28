# Gestion patch sur Linux

### 1️⃣ Installer le paquet `python3-venv` si ce n'est pas déjà fait

```bash
sudo apt install python3.12-venv
```

**Pourquoi ?**

* Ce paquet est nécessaire pour créer des **environnements virtuels Python** sur Debian/Ubuntu.
* Sans lui, Python ne peut pas isoler les paquets, et tout ce que tu installes irait directement dans le système, ce qui peut casser des programmes ou le Python du système.

---

### 2️⃣ Créer mon environnement virtuel

```bash
python3 -m venv mon_env
```

* Je choisis un nom pour mon dossier (`mon_env`).
* Cela crée un **Python isolé**, avec son propre pip et ses propres paquets.
* Pourquoi ? Pour que mes projets Python restent **indépendants**, et que je puisse installer des bibliothèques sans toucher au système.

---

### 3️⃣ Activer mon environnement

```bash
source mon_env/bin/activate
```

* L’activation change ton terminal pour utiliser **le Python de mon_env**, pas celui du système.
* Mon prompt affiche `(mon_env)` pour me rappeler que je suis dans l’environnement isolé.
* Pourquoi ? Pour que **tous mes pip install** aillent dans cet environnement, pas dans le système global.

---

### 4️⃣ Installer mes paquets avec pip

```bash
pip install requests beautifulsoup4
```

* Les paquets installés restent **dans mon_env**.
* Pourquoi ? Pour que chaque projet ait exactement les bibliothèques dont il a besoin, sans interférer avec d’autres projets ni le Python système.

---

### 5️⃣ Travailler dans mon projet

```bash
cd /chemin/vers/mon/projet
source mon_env/bin/activate
```

* Chaque fois que je reviens travailler sur ce projet, je réactive **mon_env**.
* Pourquoi ? Pour être sûr que je travaille avec les bonnes versions de Python et de bibliothèques pour ce projet précis.

---

### 6️⃣ Sortir de l’environnement

```bash
deactivate
```

* Quand j’ai fini, mon terminal revient au Python système.
* Pourquoi ? Pour ne pas utiliser accidentellement les paquets du projet dans un autre contexte.
