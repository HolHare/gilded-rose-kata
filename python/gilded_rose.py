# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue  # Sulfuras requires no changes

            # Decrease sell_in for all except Sulfuras
            item.sell_in -= 1

            # Update quality based on item type
            if item.name == "Aged Brie":
                self.update_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.update_backstage_passes(item)
            elif item.name.startswith("Conjured"):
                self.update_conjured_item(item)
            else:
                self.update_normal_item(item)

            # Ensure quality stays within bounds
            item.quality = max(0, min(50, item.quality))

    def update_aged_brie(self, item):
        # Increases by 1, and by 1 more after sell_in <0
        item.quality += 1
        if item.sell_in < 0:
            item.quality += 1

    def update_backstage_passes(self, item):
        if item.sell_in < 0:
            item.quality = 0
        else:
            item.quality += 1
            if item.sell_in < 10:
                item.quality += 1
            if item.sell_in < 5:
                item.quality += 1

    def update_conjured_item(self, item):
        degrade = 2
        if item.sell_in < 0:
            degrade *= 2
        item.quality -= degrade

    def update_normal_item(self, item):
        degrade = 1
        if item.sell_in < 0:
            degrade *= 2
        item.quality -= degrade


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
