from datetime import datetime

class TabelaLinhaMontagem:
    def __init__(
        self,
        cd_clie: str,
        cd_voss: str,
        qt_sac_plast: int,
        tp_embl_int_cd_micr_sig: str,
        qt_caixa: int,
        tp_caixa_cd_micr_sig: str,
        md_etq_sac_plast: str,
        md_etq_caixa: str,
        dt_elb: datetime,
        dt_rev: datetime,
        cd_ie: str,
        dt_crga: datetime
    ):

        if isinstance (cd_clie, str):
            raise TypeError ("O campo 'c_clie' deve ser do tipo 'string'")

        if isinstance(cd_voss, str):
            raise TypeError("O campo 'c_voss' deve ser do tipo 'string'")

        if isinstance(qt_sac_plast, int):
            raise TypeError("O campo 'qt_sac_plast' deve ser do tipo 'int'")

        if isinstance(tp_embl_int_cd_micr_sig, str):
            raise TypeError("O campo 'tp_embl_int_cd_micr_sig' deve ser do tipo 'string'")

        if isinstance(qt_caixa, int):
            raise TypeError("O campo 'qt_caixa' deve ser do tipo 'int'")

        if isinstance(tp_caixa_cd_micr_sig, str):
            raise TypeError("O campo 'tp_caixa_cd_micr_sig' deve ser do tipo 'string'")

        if isinstance(md_etq_sac_plast, str):
            raise TypeError("O campo 'md_etq_sac_plast' deve ser do tipo 'string'")

        if isinstance(md_etq_caixa, str):
            raise TypeError("O campo 'md_etq_caixa' deve ser do tipo 'string'")

        if isinstance(dt_elb, datetime):
            raise TypeError("O campo 'dt_elb' deve ser do tipo 'datetime'")

        if isinstance(dt_rev, datetime):
            raise TypeError("O campo 'dt_rev', deve ser do tipo 'datetime'")

        if isinstance(cd_ie, str):
            raise TypeError("O campo 'cd_ie' deve ser do tipo 'string'")

        if isinstance(dt_crga, datetime):
            raise TypeError("O campo 'dt_crga', deve ser do tipo 'datetime'")