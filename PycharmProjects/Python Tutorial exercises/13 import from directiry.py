#  option 1
import ecommerce.shipping

ecommerce.shipping.calc_tax()

#  option 2

from ecommerce.shipping import calc_shipping, calc_tax

calc_shipping()
calc_tax()

##############################
#  option 3

from ecommerce import shipping

shipping.calc_tax()
