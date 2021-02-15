document.getElementById('basildi').addEventListener('click', myScriptS)

function myScriptS() {
  var e = document.getElementById('naslar');
  document.getElementById('basildi').innerHTML = "YUKLENIYOR 5 DAKIKA SUREBILIR LUTFEN BEKLEYIN`"
  fetch('http://192.168.6.153:5000').then(response => response.json())
  .then(data => data.forEach(element => {

    let jsonObjesi = JSON.parse(element)
    if (jsonObjesi !== null) {
      console.log(jsonObjesi);
      var html = '';
      html += `
        <div style="background-color: transparent; "  class="card col-md-5 mb-3 mr-2 border border-warning">
            <div class="card-header text-center ">${jsonObjesi.NamesMimosa}
                                <hr style="background-color: darkorange;">
                                <div class="card-body text-left">
                                  <table class="table table-sm">
                                  <h3 class="text-center"><a href="http://${jsonObjesi.MimosaIp}/">Cihaza Git</a></h3>
                                  <thead>
                                    <tr>
                                      <th scope="col"></th>
                                      <th scope="col">Mhz</th>
                                      <th scope="col"></th>
                                      <th scope="col" class="text-right">${jsonObjesi.MimosaMhz} </th>
                                    </tr>
                                  </thead>
                                  <tbody>
                                  <tr>
                                  <th scope="row"></th>
                                  <td>Anlik Gelen  </td>
                                  <td></td>
                                  <td class="text-right">${jsonObjesi.MimosaRxValue} Mbps</td>
                                </tr>
                                    <tr>
                                      <th scope="row"></th>
                                      <td>Anlik Giden </td>
                                      <td></td>
                                      <td class="text-right">${jsonObjesi.MimosaTxValue} Mbps </td>
                                    </tr>

                                    <tr>
                                    <th scope="row"></th>
                                    <td>Frequency </td>
                                    <td></td>
                                    <td class="text-right">${jsonObjesi.MimosaFrequency}</td>
                                  </tr>

                                  <tr>
                                  <th scope="row"></th>
                                  <td>Max Gelebilecek  </td>
                                  <td></td>
                                  <td class="text-right">${jsonObjesi.MimosaTotalRxPhy} Mbps</td>
                                </tr>
                                <tr>
                                <th scope="row"></th>
                                <td>Max Gidebilecek  </td>
                                <td></td>
                                <td class="text-right">${jsonObjesi.MimosaTotalTxPhy} Mbps</td>
                              </tr>
                              <tr>
                              <th scope="row"></th>
                              <td>Sinyal Degeri Rx </td>
                              <td></td>
                              <td class="text-right">${jsonObjesi.RxDbm}</td>
                            </tr>
                            <tr>
                            <th scope="row"></th>
                            <td>Sinyal Degeri Tx </td>
                            <td></td>
                            <td class="text-right">${jsonObjesi.RxDbm1}</td>
                          </tr>
                          <tr>
                            <th scope="row"></th>
                            <td>MimosaCpuTemp </td>
                            <td></td>
                            <td class="text-right"> <i class="fas fa-temperature-high">   ${jsonObjesi.MimosaCpuTemp}</i></td>
                          </tr>
                                  </tbody>
                                </table> </div>
                            </div>
                            </div>`;
      // header += `${jsonObjesi.NamesMimosa}`
      document.getElementById('selamDur').innerHTML += html;
      document.getElementById('basildi').innerHTML = "Yuklendi"

    }

  }))
  .catch(err => console.log(err));
};


//
//          // <a href="${jsonObjesi.MimosaIp}"></a>${jsonObjesi.MimosaIp}


//                 //                           MaxRx1Kapasite:  ${jsonObjesi.MimosaRxPhy1}

//                 //                           RxDegeri  ${jsonObjesi.rxValues}
//                 //                           TxDegeri   ${jsonObjesi.txValues}
//                 //                           CpuSicaklik  ${jsonObjesi.MimosaCpuTemp}
//                 //                           ${jsonObjesi.WirelesStatus}
//                 //                           SinyalSeviyesi    ${jsonObjesi.RxDbm}
//                 //                           SinyalSeviyesi2   ${jsonObjesi.RxDbm1}