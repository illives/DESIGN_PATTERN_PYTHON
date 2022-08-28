try:
    import sys, os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../'
            )
        )
    )
except:
    raise

from Ritimo_resource.Region_01__Music_Factory import  RegionOneMusic


if __name__=='__main__':

    region_one = RegionOneMusic('rock')
    region_one.tocar_musica()