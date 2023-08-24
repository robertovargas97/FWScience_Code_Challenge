from django.core.management.base import BaseCommand, CommandError

import requests
from planets_api.models import Planet


class Command(BaseCommand):
    help = "Fetches the planets data by using a specific query and then inserts the data into a database."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # We use a generator in case that we get a huge list (maybe this is not the case, however it is better safe than sorry)
    def _fetch_planets_data_generator(self):
        """Gets the planets data according to the query defined in the request payload.

        Yields:
            planet (dict): dictionary that contains the planet information (name, population, terrains, climates)
        """
        planets_api_url = "https://swapi-graphql.netlify.app/.netlify/functions/index"
        request_headers = {"Content-Type": "application/json"}
        request_payload = {
            "query": "query Query {allPlanets{planets{name population terrains climates}}}"
        }

        response = requests.post(
            url=planets_api_url, headers=request_headers, json=request_payload
        )
        response.raise_for_status()
        planets_list = (
            response.json().get("data", {}).get("allPlanets", {}).get("planets", [])
        )

        for planet in planets_list:
            yield planet

    def handle(self, *args, **kwargs):
        try:
            for planet in self._fetch_planets_data_generator():
                new_planet = Planet(**planet)
                new_planet.save()

            self.stdout.write(self.style.SUCCESS("Planets inserted successfully."))

        except Exception as e:
            raise CommandError(
                f"There was an error while executing the command -> {str(e)}"
            )
