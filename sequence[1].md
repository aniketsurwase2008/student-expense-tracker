# Sequence Diagram — Add Expense

```text
User -> CLI: choose Add
CLI -> User: request date/category/amount/note
User -> CLI: enter values
CLI -> Service: add(values)
Service -> Validators: validate fields
Validators --> Service: validated values
Service -> Model: create Expense
Model --> Service: Expense object
Service -> Storage: save(expenses)
Storage --> Service: saved
Service --> CLI: new Expense
CLI --> User: success message
```
