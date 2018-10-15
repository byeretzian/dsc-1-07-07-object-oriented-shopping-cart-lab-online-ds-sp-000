class ShoppingCart():
    
    def __init__(self, _employee_discount = None, _total = None, _items = None):
        self._total = 0
        self._items = []
        self._employee_discount = _employee_discount
        
    def total(self):
        return self._total
    
    def items(self):
        return self._items
    
    def employee_discount(self):
        return self._employee_discount
    
    def add_item(self, item, price, quantity = 1):
        self._items.append({'item_name': item, 'price' : price, 'quantity': quantity})
        if quantity == None:
            self._total += price
        else:
            self._total += price*quantity
        return self._total
    
    def mean_item_price(self):
        price_list = []
        quantities = []
        for item in self._items:
            price_list.append(item['price']*item['quantity'])
            quantities.append(item['quantity'])
        mean = sum(price_list)/sum(quantities)
        return mean
    
    def median_item_price(self):
        prices = []
        for item in self._items:
            for i in range(item['quantity']-1):
                prices.append(item['price'])
        if len(prices)%2 == 0:
            mid1 = prices[int((len(prices)/2) - 1)]
            mid2 = prices[int((len(prices)/2))]
            median = (mid1 + mid2) / 2
        else:
            mid = (len(prices)/2) + .5
            median = prices[int[mid]]
        return median
    
    def apply_discount(self):
        if self._employee_discount == None:
            return "Sorry, there is no discount to apply to your cart :("
        else:
            discounted_total = self._total - ((0.01*self._employee_discount)*self._total)
            return discounted_total
        
    def item_names(self):
        items = []
        for item in self._items:
            for i in range (item['quantity']):
                items.append(item['item_name'])
        return items
    
    def void_last_item(self):
        if len(self._items) == 0:
            return "There are no items in your cart!"
        else:
            self._items[-1]['quantity'] -= 1
            self._total -= self._items[-1]['price']
            print(self._total)