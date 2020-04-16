payloadsGRRequest = [
    {
        "version": 36,
        "language": "de",
        "start": {
            "name": "Wartenau",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:10901",
        },
        "dest": {
            "name": "Ritterstraße",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:60904",
        },
        "toStartBy": "FOOTPATH",
        "toDestBy": "FOOTPATH",
        "time": {"date": "heute", "time": "jetzt"},
        "timeIsDeparture": True,
        "schedulesBefore": 0,
        "schedulesAfter": 4,
        "intermediateStops": True,
        "tariffInfoSelector": [
            {"tariff": "HVV", "tariffRegions": True, "kinds": ["1"]},
            {"tariff": "SH", "tariffRegions": False, "kinds": ["1"]},
        ],
        "penalties": [
            {
                "name": "desiredType",
                "value": "longdistancebus,fasttrain&extrafasttrain:10000",
            }
        ],
        "returnContSearchData": True,
        "realtime": "REALTIME",
    },
    {
        "start": {
            "name": "Wartenau",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:10901",
        },
        "dest": {
            "name": "Ritterstraße",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:60904",
        },
    },
    {
        "start": {
            "name": "Wartenau",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:10901",
        },
        "dest": {
            "name": "Ritterstraße",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:60904",
        },
        "timeIsDeparture": False,
    },
    {
        "start": {
            "name": "Wartenau",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:10901",
        },
        "dest": {
            "name": "Ritterstraße",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:60904",
        },
        "penalties": [
            {
                "name": "desiredType",
                "value": "longdistancebus,fasttrain&extrafasttrain:10000",
            },
            {"name": "ToStartStationBy", "value": "1",},
            {"name": "TimeRange", "value": "100",},
            {"name": "ForVisitors", "value": "1",},
        ],
    },
    # Requests from hvv website
    {
        "version": 36,
        "language": "de",
        "start": {
            "name": "Von-Sauer-Straße",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:80101",
        },
        "dest": {
            "name": "Beethovenstraße",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:70036",
        },
        "toStartBy": "FOOTPATH",
        "toDestBy": "FOOTPATH",
        "time": {"date": "heute", "time": "jetzt"},
        "timeIsDeparture": True,
        "schedulesBefore": 0,
        "schedulesAfter": 4,
        "intermediateStops": True,
        "tariffInfoSelector": [
            {"tariff": "HVV", "tariffRegions": True, "kinds": ["1"]},
            {"tariff": "SH", "tariffRegions": False, "kinds": ["1"]},
        ],
        "penalties": [
            {
                "name": "desiredType",
                "value": "longdistancebus,fasttrain&extrafasttrain:10000",
            }
        ],
        "returnContSearchData": True,
        "realtime": "REALTIME",
    },
    {
        "version": 36,
        "language": "en",
        "start": {
            "name": "Hamburg-Harburg",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:8000147",
        },
        "dest": {
            "name": "Stade",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:8000089",
        },
        "toStartBy": "FOOTPATH",
        "toDestBy": "FOOTPATH",
        "time": {"date": "heute", "time": "jetzt"},
        "timeIsDeparture": True,
        "schedulesBefore": 0,
        "schedulesAfter": 4,
        "intermediateStops": True,
        "tariffInfoSelector": [
            {"tariff": "HVV", "tariffRegions": True, "kinds": ["1"]},
            {"tariff": "SH", "tariffRegions": False, "kinds": ["1"]},
        ],
        "penalties": [
            {
                "name": "desiredType",
                "value": "longdistancebus,fasttrain&extrafasttrain:10000",
            }
        ],
        "returnContSearchData": True,
        "realtime": "REALTIME",
    },
    {
        "version": 36,
        "language": "de",
        "start": {
            "name": "Modering",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:86004",
        },
        "dest": {
            "name": "Stade",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:8000089",
        },
        "toStartBy": "FOOTPATH",
        "toDestBy": "FOOTPATH",
        "time": {"date": "13.02.2020", "time": "14:24"},
        "timeIsDeparture": True,
        "schedulesBefore": 0,
        "schedulesAfter": 4,
        "intermediateStops": True,
        "tariffInfoSelector": [
            {"tariff": "HVV", "tariffRegions": True, "kinds": ["1"]},
            {"tariff": "SH", "tariffRegions": False, "kinds": ["1"]},
        ],
        "penalties": [
            {
                "name": "desiredType",
                "value": "longdistancebus,fasttrain&extrafasttrain:10000",
            }
        ],
        "returnContSearchData": True,
        "realtime": "REALTIME",
    },
    {
        "version": 36,
        "language": "de",
        "start": {
            "name": "Modering",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:86004",
        },
        "dest": {
            "name": "Stade",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:8000089",
        },
        "toStartBy": "FOOTPATH",
        "toDestBy": "FOOTPATH",
        "time": {"date": "13.02.2020", "time": "14:24"},
        "timeIsDeparture": True,
        "schedulesBefore": 0,
        "schedulesAfter": 4,
        "intermediateStops": True,
        "tariffInfoSelector": [
            {"tariff": "HVV", "tariffRegions": True, "kinds": ["1"]},
            {"tariff": "SH", "tariffRegions": False, "kinds": ["1"]},
        ],
        "penalties": [
            {
                "name": "desiredType",
                "value": "akn,r,re,longdistancebus,ast,fasttrain&extrafasttrain:10000",
            }
        ],
        "returnContSearchData": True,
        "realtime": "REALTIME",
    },
    {
        "version": 36,
        "language": "de",
        "start": {
            "name": "Modering",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:86004",
        },
        "via": {
            "name": "Hauptbahnhof",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:9910910",
        },
        "dest": {
            "name": "Stade",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:8000089",
        },
        "toStartBy": "BICYCLE",
        "toDestBy": "FOOTPATH",
        "time": {"date": "13.02.2020", "time": "14:24"},
        "timeIsDeparture": True,
        "schedulesBefore": 0,
        "schedulesAfter": 4,
        "intermediateStops": True,
        "tariffInfoSelector": [
            {"tariff": "HVV", "tariffRegions": True, "kinds": ["1"]},
            {"tariff": "SH", "tariffRegions": False, "kinds": ["1"]},
        ],
        "penalties": [
            {
                "name": "desiredType",
                "value": "akn,r,re,longdistancebus,ast,fasttrain&extrafasttrain:10000",
            },
            {"name": "AnyHandicap", "value": "5"},
            {"name": "ExtraFare", "value": "0"},
            {"name": "DesiredLine", "value": "S1:1"},
        ],
        "returnContSearchData": True,
        "realtime": "REALTIME",
    },
    {
        "version": 36,
        "language": "de",
        "start": {
            "name": "Wartenau",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:10901",
        },
        "via": {
            "name": "Hausbruch",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:41033",
        },
        "dest": {
            "name": "U Ritterstraße",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:60012",
        },
        "forcedStart": {
            "name": "Celsiusweg",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:80114",
        },
        "forcedDest": {
            "name": "Modering",
            "city": "",
            "combinedName": "",
            "type": "STATION",
            "id": "Master:86004",
        },
        "toStartBy": "BICYCLE",
        "toDestBy": "FOOTPATH",
        "time": {"date": "15.02.2020", "time": "15:38"},
        "timeIsDeparture": True,
        "schedulesBefore": 0,
        "schedulesAfter": 4,
        "intermediateStops": True,
        "tariffInfoSelector": [
            {"tariff": "HVV", "tariffRegions": True, "kinds": ["1"]},
            {"tariff": "SH", "tariffRegions": False, "kinds": ["1"]},
        ],
        "penalties": [
            {
                "name": "desiredType",
                "value": "longdistancebus,fasttrain&extrafasttrain:10000",
            },
            {"name": "AnyHandicap", "value": "-1"},
            {"name": "ChangeEvent", "value": "0"},
            {"name": "Walker", "value": "0"},
            {"name": "ExtraFare", "value": "0"},
            {"name": "DesiredLine", "value": "A1:1"},
        ],
        "returnContSearchData": True,
        "realtime": "REALTIME",
    },
]

payloadsCNRequest = [
    {
        "version": 36,
        "theName": {
            "name": "Wartenau",
            "city": "Hamburg",
            "combinedName": "",
            "type": "STATION",
        },
        "maxList": 1,
        "allowTypeSwitch": False,
    },
    {
        "version": 36,
        "theName": {
            "name": "U Ritterstraße",
            "city": "Hamburg",
            "combinedName": "",
            "type": "STATION",
        },
        "maxList": 1,
        "allowTypeSwitch": False,
    },
    {"theName": {"name": "Stade"}},
]


payloadsTariffRequest = [
    {
        "language": "de",
        "version": 37,
        "scheduleElements": [
            {
                "departureStationId": "Master:10950",
                "arrivalStationId": "Master:37979",
                "lineId": "DB-EFZ:RE8_DB-EFZ_Z",
            }
        ],
        "departure": {"date": "16.02.2020", "time": "8:04"},
        "arrival": {"date": "16.02.2020", "time": "8:29"},
    },
    {
        "version": 36,
        "language": "de",
        "departure": {"date": "15.02.2020", "time": "15:37"},
        "arrival": {"date": "15.02.2020", "time": "15:39"},
        "scheduleElements": [
            {
                "lineId": "HHA-U:U1_HHA-U",
                "departureStationId": "Master:10901",
                "arrivalStationId": "Master:60904",
            }
        ],
        "returnReduced": True,
    },
    {
        "version": 36,
        "language": "de",
        "departure": {"date": "15.02.2020", "time": "15:57"},
        "arrival": {"date": "15.02.2020", "time": "16:41"},
        "scheduleElements": [
            {
                "lineId": "ZVU-DB:S1_ZVU-DB_S-ZVU",
                "departureStationId": "Master:80954",
                "arrivalStationId": "Master:11950",
            },
            {
                "lineId": "HHA-U:U2_HHA-U",
                "departureStationId": "Master:11950",
                "arrivalStationId": "Master:10952",
            },
            {
                "lineId": "HHA-U:U3_HHA-U",
                "departureStationId": "Master:10952",
                "arrivalStationId": "Master:70903",
            },
        ],
        "returnReduced": True,
    },
    {
        "version": 36,
        "language": "de",
        "departure": {"date": "15.02.2020", "time": "16:13"},
        "arrival": {"date": "15.02.2020", "time": "17:50"},
        "scheduleElements": [
            {
                "lineId": "HHA-B:151_HHA-B",
                "departureStationId": "Master:52002",
                "arrivalStationId": "Master:54006",
            },
            {
                "lineId": "ZVU-DB:S31_ZVU-DB_S-ZVU",
                "departureStationId": "Master:54951",
                "arrivalStationId": "Master:49950",
            },
            {
                "lineId": "DB-EFZ:RE3_DB-EFZ_Z",
                "departureStationId": "Master:8000147",
                "arrivalStationId": "Master:8000238",
            },
            {
                "lineId": "KVGMa:5009_KVGMa_KVGMAS",
                "departureStationId": "Master:25080",
                "arrivalStationId": "Master:15097",
            },
        ],
        "returnReduced": True,
    },
]
