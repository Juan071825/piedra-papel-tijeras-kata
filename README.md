# ÍNDICE
<ul>
<li><a href='#introduccion'>Introducción</a></li>
<li><a href='#manual'>Manual</a></li>
<li><a href='#metodologia'>Metodología</a></li>

</ul><hr/>

## <div id= 'introduccion'>Introducción</div>

Juan Mateo Álvarez Álvarez  - <a href='https://github.com/Juan071825'>@Juan071825</a> <br/>
Adrián González González    - <a href= 'https://github.com/Adriceka'>@Adriceka</a>

## <div id='manual'>Manual</div>

### Instalación

```bash
git clone https://github.com/Juan071825/piedra-papel-tijeras-kata.git
```

### Entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate  # En Linux / Mac
venv\Scripts\activate     # En Windows
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```


## <div id='metodologia'>Metodología</div>

La metodología empleada está inspirada en el enfoque de Desarrollo Guiado por Pruebas (TDD).

### Proceso seguido:

1. Definir las reglas del juego como requisitos.
2. Crear los casos test.
3. Implementar la lógica hasta que todos los tests pasen.
4. Refactorizar aplicando principios SOLID.


---

### Estructura del proyecto

```
src/
 ├── RPS_dict.py
main.py
tests/
 ├── test_RSP.py
pytest.ini
```

### Principios aplicados

- SRP (Single Responsibility Principle)
- OCP (Open Closed Principle)
- Separación de lógica y presentación

---

