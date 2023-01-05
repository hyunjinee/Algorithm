# 1357. Apply Discount Every n Orders

![nn](https://user-images.githubusercontent.com/63354527/109947563-cbff6200-7d1c-11eb-8043-8a70ee7a8eec.PNG)

```typescript
class Cashier {
  // attributes
  private n: number;
  private discount: number;
  private count: number;
  private price: Map<number, number>;

  constructor(
    n: number,
    discount: number,
    products: number[],
    prices: number[]
  ) {
    // set attrs
    this.n = n;
    this.discount = discount;
    this.count = 0;
    this.price = new Map();

    // iterate thru products/prices, and set the price for each product in map
    for (let i = 0; i < prices.length; i++)
      this.price.set(products[i], prices[i]);
  }

  getBill(product: number[], amount: number[]): number {
    // first, get total cost of this order (pre-discount)
    let cost = 0;
    for (let i = 0; i < product.length; i++)
      cost += this.price.get(product[i])! * amount[i];

    // now, determine if this customer gets a discount (they are nth customer)
    return ++this.count % this.n === 0
      ? cost * (1 - this.discount / 100)
      : cost;
  }
}
```
