import poller


def test_get_ha_id_from_valid_ha_name():
    name = "climate.bathroom"
    assert (poller.get_ha_id_from_ha_name(name)) == "OEQ0443348"


def test_get_ha_id_from_incorrect_ha_name():
    name = "climate.voodoo"
    assert (poller.get_ha_id_from_ha_name(name)) == "Not Found"


def test_get_climate_devices_from_home_assistant():
    climate_devices = poller.get_climate_devices_from_home_assistant()
    for row in climate_devices:
        print (row)
        assert row.startswith("climate") == True


def test_get_target_temps_from_home_assistant():
    target_temps = poller.get_target_temps_from_home_assistant()
    for row in target_temps:
        print (target_temps[row])
        assert isinstance(target_temps[row], float) == True

