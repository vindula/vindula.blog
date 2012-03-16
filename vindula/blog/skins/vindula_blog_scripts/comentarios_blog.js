$j = jQuery.noConflict();

function ajax_comentarios(){    
    var estados = []
    $j('[name=review_state]:checked').each(function(){
        estados.push($j(this).val());
    });
    if (estados.length<1){estados.push('None')}

    jq.post('comentarios_blog_pendentes',
           {review_state:estados},
           function(data){
                $j('#listagem_comentarios').html(data);
                ajusta_total();
           }
    );
}

function marcar_comentarios(){    
    if ($j(this).hasClass('aprovar')){
        if ($j(this).hasClass('todos')){
            $j('.aprovado').attr('checked','checked');
        }else{
            $j('.aprovado:checked').attr('checked','');
        }
    }else{
        if ($j(this).hasClass('todos')){
            $j('.reprovado').attr('checked','checked');
        }else{
            $j('.reprovado:checked').attr('checked','');
        }
    }
}

function ajusta_total(){
    var pendentes =  parseFloat($j('#num_pendentes').attr('value'));
    var aprovados = parseFloat($j('#num_aprovados').attr('value'));
    var reprovados = parseFloat($j('#num_reprovados').attr('value'));

    $j('#total_pendente').html(pendentes);
    $j('#total_aprovado').html(aprovados);
    $j('#total_reprovado').html(reprovados);
    $j('#total_comentario').html(parseInt($j('#num_pendentes').attr('value'))+parseInt($j('#num_aprovados').attr('value'))+parseInt($j('#num_reprovados').attr('value')));
}

$j(document).ready(function(){
    $j('.marcacao').click(marcar_comentarios);
    $j('[name=review_state]').change(ajax_comentarios);
    $j('#btn_aplicar').click(function(){
        $j('#form_comentarios').submit();
    });    
    ajusta_total();
});