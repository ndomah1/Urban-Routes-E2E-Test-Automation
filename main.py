import data
import helpers


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        """Runs once before all tests to ensure the Urban Routes server is reachable."""
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        """Stub for testing setting a route"""
        # Add in S8
        print("function created for set route")
        pass

    def test_select_plan(self):
        """Stub for testing selecting a plan"""
        # Add in S8
        print("function created for select plan")
        pass

    def test_fill_phone_number(self):
        """Stub for testing filling phone number"""
        # Add in S8
        print("function created for fill phone number")
        pass

    def test_fill_card(self):
        """Stub for testing filling card information"""
        # Add in S8
        print("function created for fill card")
        pass

    def test_comment_for_driver(self):
        """Stub for testing commenting for driver"""
        # Add in S8
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        """Stub for testing ordering blanket and handkerchiefs"""
        # Add in S8
        print("function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        """Stub for testing ordering two ice creams"""
        print("function created for order 2 ice creams")
        for _ in range(2):
            # Add in S8
            pass

    def test_car_search_model_appears(self):
        """Stub for testing that car search model appears"""
        # Add in S8
        print("function created for car search model appears")
        pass
