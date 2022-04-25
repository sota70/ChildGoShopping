"""
おつかい処理を行う時に使うクラス

property money: 所持金
"""
class Child:

    """
    クラスのプロパティの初期化を行うメソッド
    クラス呼び出し時に所持金を入力することが要求される

    parameter _money: 所持金
    """
    def __init__(self, _money: int):
        self.money = _money

    """
    おつかいに行くメソッド
    指定された商品を一つ買ったあと、もう一つの指定された商品を
    限度額になるまで買う

    parameter shop: お店にある商品とその金額一覧
    parameter targetItem1: おつかいで買ってくる商品1つ目
    parameter targetItem2: おつかいで買ってくる商品2つ目
    """
    def goShopping(
        self, 
        shop: dict[str, int],  
        targetItem1: str, 
        targetItem2: str
    ):
        self.buyTargetItem(shop, targetItem1)
        self.keepBuyingTargetItem(shop, targetItem2)

    """
    指定された商品があった場合それを１つ買うメソッド

    parameter shop: お店にある商品とその金額一覧
    parameter targetItem: 買ってくる商品
    """
    def buyTargetItem(self, shop: dict[str, int], targetItem: str):
        shopItems = shop.keys()
        if not targetItem in shopItems: return
        print(targetItem + "を買った")
        targetItemPrice = shop[targetItem]
        self.money -= targetItemPrice

    """
    指定された商品があった場合それを複数個買うメソッド
    所持金が事前に定めた限度額になるまで商品を買い続ける

    parameter shop: お店にある商品とその金額一覧
    parameter targetItem: 買ってくる商品
    """
    def keepBuyingTargetItem(self, shop: dict[str, int], targetItem: str):
        shopItems = shop.keys()
        if not targetItem in shopItems: return
        targetItemPrice = shop[targetItem]
        while self.money >= 120:
            print(targetItem + "を買った")
            self.money -= targetItemPrice