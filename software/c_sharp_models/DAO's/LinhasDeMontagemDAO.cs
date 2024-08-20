using c_sharp_models.Models;
using System;
using System.Collections.Generic;
using System.Data.SqlClient;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace c_sharp_models.DAO_s
{
    public class LinhasDeMontagemDAO
    {
        public void Inserir(LinhasDeMontagemViewModel linha, UsuarioConexaoBancoDeDadosViewModel login)
        {

            ConexaoDB conexaoDB = new ConexaoDB();
            SqlConnection conexao = conexaoDB.Conectar(login);



            conexao.Close();
        }
    }
}
