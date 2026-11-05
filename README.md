# Warehouse tools

Small Python utilities for warehouse order and shipping workflows.

Run the tests with `python3 -m unittest discover -s tests -v`.

## Shipping

`shipping_quote(weight_kg, zone, service="standard")` returns a delivery quote
in US dollars.

| Parameter  | Values                     | Notes                                  |
|------------|----------------------------|----------------------------------------|
| weight_kg  | positive float             | Parcel weight in kilograms             |
| zone       | `"local"`, `"regional"`    | Delivery zone                          |
| service    | `"standard"`, `"express"`  | Express adds a flat $7.00 surcharge    |

Unknown zones or services raise `ValueError`.

### CLI

```
python -m warehouse.cli <weight_kg> <zone> [--service {standard,express}]
```

Examples:

```bash
# Standard quote – 3 kg to a regional zone
python -m warehouse.cli 3 regional
# $12.50

# Express quote – same shipment
python -m warehouse.cli 3 regional --service express
# $19.50
```
