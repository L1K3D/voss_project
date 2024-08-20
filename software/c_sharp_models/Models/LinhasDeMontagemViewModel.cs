using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace c_sharp_models.Models
{
    public class LinhasDeMontagemViewModel()
    {

        public string cd_clie { get; set; }
        public string cd_voss { get; set; }
        public int qt_sac_plast { get; set; }
        public string tp_embl_int_cd_micr_sig { get; set; }
        public int qt_caixa { get; set; }
        public string tp_caixa_cd_micr_sig { get; set; }
        public string md_etq_sac_plast { get; set; }
        public string md_etq_caixa { get; set; }
        public DateTime dt_elb { get; set; }
        public DateTime dt_rev { get; set; }
        public string cd_ie { get; set; }
        public DateTime dt_crga { get; set; }

    }
}
