SELECT
    INITCAP(
        pkg_mdlecmarcequimedi.fVAGetNOMBRE (
            pkg_mdlecequipmedic.fNUGetIDMARCA (lecon.idequipo, 1),
            1
        )
    ) MARCA,
    lecon.lect_anterior LECTURAANTERIOR,
    lecon.idequipo IDEQUIPO,
    lecon.lect_actual LECTURAACTUAL,
    INITCAP(
        pkg_mdlectipocobro.fVAGetNOMBRE (lecon.idtipocobro)
    ) TIPO,
    lecon.consumo CONSUMO,
    '' DIAMETRO,
    lecon.consuprome CONSUPROME,
    pkg_mdfapericonsu.fDAGetFECHAINI (
        pkg_mdfaperiodo.fNUGetIDFAPERICONSU (&PERIODO, 1),
        1
    ) FECHAINI,
    pkg_mdfapericonsu.fDAGetFECHAFIN (
        pkg_mdfaperiodo.fNUGetIDFAPERICONSU (&PERIODO, 1),
        1
    ) FECHAFIN
FROM
    caproductos caprod,
    caproducmedi caprodu,
    mepuntomedi mepunto,
    leconsumos lecon
WHERE
--  caprod.idcontrato = &CONTRATO
    1=1
    AND caprod.idservicio = 1
    AND caprod.idproducto = caprodu.idproducto
    AND mepunto.idpuntomedi = caprodu.idpuntomedi
    AND mepunto.idpuntomedi = lecon.idpuntomedi
    AND lecon.idperiodo = pkg_mdfaperiodo.fNUGetIDFAPERICONSU (&PERIODO, 1);
    
---
-- SELECT * FROM leconsumos lecon  ORDER BY 1 DESC;
