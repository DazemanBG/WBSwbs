# CREADO POR::Pewati5 / DazemanBG
# 2023
# Wbs Not for real or serious purposes, just a # project.
import os
import time

mem = {
    "x": 0,
    "y": 0,
    "z": 0,
    "lcmp":0, 
    "inclu": [],
    "az": " ",
    "bz": " ",
    "cz": " ",
    "dz": " ",
}


def exe_pass(tokens):
  if len(tokens) == 4 and tokens[0] == "PASS" and tokens[2] == "TO":
    value_v = tokens[1]
    end_v = tokens[3]
    if value_v and end_v not in mem:
      print("$ERROR DE ARGUMENTO:PASS$")
    else:
      mem[end_v] = value_v
  else:
    print("$ERROR DE USO:PASS$")


def exe_move(tokens):
  if len(tokens) == 4 and tokens[0] == "MOVE" and tokens[2] == "TO":
    value_v = int(tokens[1])
    endv = tokens[3]
    if endv in mem:
      mem[endv] = value_v
    else:
      print("$ERROR DE ARGUMENTO:MOVE$")
  else:
    print("$ERROR DE USO:MOVE$")


def exe_defs(tokens): 
  if len(tokens) == 4 and tokens[0] == "DEFS" and tokens[2] == "IN":
    string_v = tokens[1].replace("@", " ")
    destination_v = tokens[3]
    if destination_v not in mem:
      print("$ERROR DE ARGUMENTO:DEFS$")
    else:
      mem[destination_v] = string_v
  else:
    print("$ERROR DE USO:DEFS$")


def exe_clear(tokens):
  if len(tokens) == 1 and tokens[0] == "CLEAR":
    os.system("clear")
  else:
    print("$ERROR DE USO:CLEAR$")


def exe_wait(tokens):
  if len(tokens) == 2 and tokens[0] == "WAIT":
    timetowait = int(tokens[1])
    time.sleep(timetowait)
  else:
    print("$ERROR DE USO:WAIT$")


def exe_print(tokens):
  if len(tokens) == 2 and tokens[0] == "PRINT":
    args_v = tokens[1]
    if args_v not in mem:
      print("$ERROR DE ARGUMENTO:PRINT$")
    else:
      print(mem[args_v])


def exe_create(tokens):
  #SOLO PARA STRINGS SI QUIERES MANEJAR NUMEROS USA X,Y,Z
  if len(tokens) == 3 and tokens[0] == "CREATE":
    name_vv = str(tokens[1])
    val_vv = str(tokens[2].replace("@", " "))
    mem[name_vv] = val_vv
  else:
    print("$ERROR DE USO:CREATE$")


def exe_cmp(tokens):
  #CMP a AND b
  if len(tokens) == 4 and tokens[0] == "CMP" and tokens[2] == "AND":
    valuecmp1 = tokens[1]
    valuecmp2 = tokens[3]
    if valuecmp1 and valuecmp2 not in mem:
      print("$ERROR DE ARGUMENTO:CMP$")
    else:
      if mem[valuecmp1] > mem[valuecmp2]:
        mem["lcmp"] = 1
      elif mem[valuecmp1] < mem[valuecmp2]:
        mem["lcmp"] = 2
      elif mem[valuecmp1] == mem[valuecmp2]:
        mem["lcmp"] = 3
      else:
        print("$ERROR DE ASIGNACION:CMP$")
  else:
    print("$ERROR DE USO:CMP$")


def beg_begin(tokens):
  if len(tokens) == 1 and tokens[0] == "BEGIN":
    print("$<")
  else:
    pass  # no es un comando realmente importante solo muestra donde


def adds_includes(tokens):
  if len(tokens) == 2 and tokens[0] == "INCLUDE":
    includeArgs = tokens[1]
    mem["inclu"].append(includeArgs)
  else:
    print("$ERROR DE USO:INCLUDE$")


def adds_call(tokens):
  if len(tokens) == 2 and tokens[0] == "CALL":
    archname = tokens[1]
    if archname in mem["inclu"]:
      read_arch(archname)
    else:
      print("$ERROR DE ARGUMENTO:CALL$")

  else:
    print("$ERROR DE USO:CALL$")


def alt_puts(tokens):
  if len(tokens) == 2 and tokens[0] == "PUTS":
    print(tokens[1].replace("@", " "))
  else:
    print("$ERROR DE USO:PUTS$")


def read_arch(archname):
  ext = os.path.splitext(archname)[1]
  if ext == ".wbs":
    try:
      with open(archname, "r") as arch:
        for linea in arch:
          tokens = linea.split()
          if len(tokens) > 0:
            if tokens[0] == "END":
              print(">$")
            if tokens[0] == "BEGIN":
              beg_begin(tokens)
            if tokens[0] == "MOVE":
              exe_move(tokens)
            if tokens[0] == "TAB":
              for var_v, val_v in mem.items():
                print(f"$VAR [{var_v}]: VAL[{val_v}]$\n")
            if tokens[0] == "PASS":
              exe_pass(tokens)
            if tokens[0] == "DEFS":
              exe_defs(tokens)
            if tokens[0] == "CLEAR":
              exe_clear(tokens)
            if tokens[0] == "WAIT":
              exe_wait(tokens)
            if tokens[0] == "PRINT":
              exe_print(tokens)
            if tokens[0] == "CREATE":
              exe_create(tokens)
            if tokens[0] == ";":
              pass
            if tokens[0] == "CMP":
              exe_cmp(tokens)
            if tokens[0] == "PUTS":
              alt_puts(tokens)
            if tokens[0] == "INCLUDE":
              adds_includes(tokens)
            if tokens[0] == "CALL":
              adds_call(tokens)
            else:
              continue

    except FileNotFoundError:
      print(f"$El archivo {archname} no existe.$")
      start()
  else:
    print(f"El archivo {archname} no es compatible con el programa")
    start()


def start():
  archivename = input("$INGRESA EL NOMBRE DE TU ARCHIVO:$ \n")
  read_arch(archivename)


def mainProg():
  inc = input("#LISTO#\n")
  if inc == "EXE":
    start()
    mainProg()
  elif inc == "TAB":
    for var_v, val_v in mem.items():
      print(f"$VAR [{var_v}]: VAL[{val_v}]$")
    mainProg()
  elif inc == "KILL":
    print("PROGRAMA FINALIZADO")
  else:
    print(f"#EL COMANDO '{inc}' NO EXISTE#")
    mainProg()


mainProg()