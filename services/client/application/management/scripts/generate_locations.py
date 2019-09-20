from application.models import Location, Coordinates


def generate_location():
    try:
        location = Location.objects.first()
        if not location:
            coordinates = Coordinates(latitude=-23.554189, longitude=-46.662206)
            coordinates.save()
            location = Location(
                street="Av. Angélica",
                street_number=2529,
                info="inovabra habitat",
                neighborhood="Bela Vista",
                city="São Paulo",
                state="SP",
                country="BR",
                zip_code="01227200",
                coordinates=coordinates
            )
            location.save()
        return location
    except Exception as e:
        print("Exceção ao tentar gerar localização: ", e)
        return None
