categoria = input("¿Qué deseas consultar? (artista, película, serie): ").strip().lower()

match categoria:
    case "artista":
        nombre = input("Ingresa el nombre del artista (Taylor Swift, Bad Bunny, Adele, Drake, Shakira): ").strip().title()
        match nombre:
            case "Taylor Swift": print("Género: Pop/Country. Álbum famoso: 1989.")
            case "Bad Bunny": print("Género: Urbano/Reggaetón. Álbum famoso: Un Verano Sin Ti.")
            case "Adele": print("Género: Soul/Pop. Álbum famoso: 21.")
            case "Drake": print("Género: Hip-Hop/Rap. Álbum famoso: Take Care.")
            case "Shakira": print("Género: Pop/Latino. Álbum famoso: Pies Descalzos.")
            case _: print("Artista no encontrado.")
    case "película" | "pelicula":
        nombre = input("Ingresa la película (Inception, Titanic, Avatar, Matrix, Shrek): ").strip().title()
        match nombre:
            case "Inception": print("Director: Christopher Nolan. Año: 2010.")
            case "Titanic": print("Director: James Cameron. Año: 1997.")
            case "Avatar": print("Director: James Cameron. Año: 2009.")
            case "Matrix": print("Directores: Hermanas Wachowski. Año: 1999.")
            case "Shrek": print("Director: Andrew Adamson. Año: 2001.")
            case _: print("Película no encontrada.")
    case "serie":
        nombre = input("Ingresa la serie (Breaking Bad, Friends, Stranger Things, The Office, Naruto): ").strip().title()
        match nombre:
            case "Breaking Bad": print("Temática: Crimen/Drama. Temporadas: 5.")
            case "Friends": print("Temática: Comedia. Temporadas: 10.")
            case "Stranger Things": print("Temática: Ciencia Ficción. Temporadas: 4.")
            case "The Office": print("Temática: Falso documental/Comedia. Temporadas: 9.")
            case "Naruto": print("Temática: Anime/Acción. Temporadas: Varios arcos.")
            case _: print("Serie no encontrada.")
    case _:
        print("Categoría no válida.")
