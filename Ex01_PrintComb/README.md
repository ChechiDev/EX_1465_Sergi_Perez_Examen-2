# Ex01: PrintComb

## Objetivo:

Escribir un programa en Python que muestre todas las combinaciones posibles de **tres dígitos distintos** en orden **estrictamente creciente**, utilizando listas y estructuras de control.

## Requisitos funcionales:

1. El programa debe generar todas las combinaciones de tres dígitos (del 0 al 9) **sin repetir dígitos** y donde cada combinación cumpla que el primer dígito < segundo dígito < tercer dígito.
   Ejemplo válido: `027`
   Ejemplo inválido: `272`, `321`, `999`.

2. El programa debe **preguntar al usuario** si desea que las combinaciones se muestren en:

   - Orden **normal** (de menor a mayor): `012, 013, 014, ..., 789`
   - Orden **invertido** (de mayor a menor): `789, 788, ..., 012`

3. El resultado debe mostrarse en pantalla, separado por comas, en una sola línea.

4. Debe usarse el siguiente prototipo de funciones:

```python
def print_comb(invertido=False):
```

```python
def main():
```

5. El programa debe ejecutarse **únicamente** cuando se llame directamente desde el terminal, usando:

```python
if __name__ == "__main__":
    main()
```

---

## Requisitos técnicos:

- No se permite usar **`itertools`**, **`set`**, **`sorted`**, **`sort()`**, ni funciones similares de ordenación o filtrado automático.
- Solo se debe utilizar **listas**, **bucles for**, y estructuras de control como `if`.
- El orden invertido debe implementarse **manualmente**, sin usar `[::-1]` ni `.reverse()`.

---

## Resultado esperado:

```bash
$ python print_comb.py
¿Quieres ver las combinaciones en orden invertido? (s/n): n
012, 013, 014, ..., 789

$ python print_comb.py
¿Quieres ver las combinaciones en orden invertido? (s/n): s
789, 788, 787, ..., 012
```
