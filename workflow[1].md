# Process Flow / Workflow

```text
START
  |
  v
Load expenses from JSON
  |
  v
Show menu
  |
  +--> Add --> validate input --> create Expense --> save JSON --+
  |                                                              |
  +--> List --> read current expenses ---------------------------+
  |                                                              |
  +--> Delete --> find ID --> delete if found --> save JSON ----+
  |                                                              |
  +--> Analytics --> aggregate by category/month --> display ----+
  |                                                              |
  +--> Exit --> END
  |
  +--> Invalid option --> show error --> menu
```
