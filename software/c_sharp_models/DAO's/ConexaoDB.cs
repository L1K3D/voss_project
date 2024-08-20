using c_sharp_models.Models;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace c_sharp_models.DAO_s
{

    public class ConexaoDB
    {

        public SqlConnection Conectar(UsuarioConexaoBancoDeDadosViewModel login)
        {
        
            string strCon = String.Format("Data Source = {1}; DataBase=b_voss_br_instrucoes_embalagem_mbb; user id={2}; password={3}",

                                           login.nome_servidor, 
                                           login.nome_login, 
                                           login.senha_login);
            SqlConnection conexao = new SqlConnection(strCon);
            conexao.Open();
            return conexao;
        
        }

    }
}
