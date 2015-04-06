
from seclang.sec_operator import SecOperator

class geolookup(SecOperator):
    def evaluate(self, input, transaction):
        if str(input) == "":
            return False

        try:
            import GeoIP
            gi = GeoIP.open("GeoIP.dat", GeoIP.GEOIP_STANDARD)
            z = gi.record_by_addr(str(input))
            return not z == None
        except:
            raise BaseException("GeoIP is not supported")

