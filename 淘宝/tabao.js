function get_timeandsign(cookie,n_param){
    // var document_cookie = 'cna=M3x0HA2AhSMCAWenhh3c24OL; tracknick=tb6382047342; _cc_=VFC%2FuZ9ajQ%3D%3D; thw=cn; lgc=tb6382047342; useNativeIM=false; mt=ci=-1_0; t=eeb6eb7465467902f5e249f1aec08d86; xlly_s=1; _m_h5_tk=8a92767226befcaac1184a25eeb769c0_1682498301257; _m_h5_tk_enc=d383d20cf51c3b39134b21db39e89a64; _tb_token_=f57fe634a3338; uc1=cookie14=Uoe8iCUiFxPFqw%3D%3D; SL_G_WPT_TO=zh-CN; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1; tfstk=cbkCB_jPHwbCnA9lKytZCZCSiBw5ZyKbbT4KAeoTTLYlrziCidX4lEhbfN2z2l1..; l=fBObBlJnLVk1EYVQBOfZPurza77TbIRA_uPzaNbMi9fPOm1p5WMNW1NOab89CnGVF6RDR3kOuRA9BeYBqIccSQLy2j-la9Mmnm9SIEf..; isg=BOPj1fhqg4JvF0kkSJbx0zwncieN2Hca1MaD6RVAJMK5VAN2naqvaguGSiTac88S'
    // var n_data = '{"appId":"34385","params":"{\\"isBeta\\":\\"false\\",\\"grayHair\\":\\"false\\",\\"appId\\":\\"30515\\",\\"from\\":\\"nt_history\\",\\"brand\\":\\"HUAWEI\\",\\"info\\":\\"wifi\\",\\"index\\":\\"4\\",\\"ttid\\":\\"600000@taobao_pc_10.7.0\\",\\"needTabs\\":\\"true\\",\\"rainbow\\":\\"\\",\\"areaCode\\":\\"CN\\",\\"vm\\":\\"nw\\",\\"schemaType\\":\\"auction\\",\\"elderHome\\":\\"false\\",\\"device\\":\\"HMA-AL00\\",\\"isEnterSrpSearch\\":\\"true\\",\\"countryNum\\":\\"156\\",\\"newSearch\\":\\"false\\",\\"network\\":\\"wifi\\",\\"subtype\\":\\"\\",\\"hasPreposeFilter\\":\\"false\\",\\"prepositionVersion\\":\\"v2\\",\\"client_os\\":\\"Android\\",\\"gpsEnabled\\":\\"false\\",\\"searchDoorFrom\\":\\"srp\\",\\"debug_rerankNewOpenCard\\":\\"false\\",\\"homePageVersion\\":\\"v7\\",\\"searchElderHomeOpen\\":\\"false\\",\\"search_action\\":\\"initiative\\",\\"sugg\\":\\"_4_1\\",\\"m\\":\\"pc\\",\\"sversion\\":\\"13.6\\",\\"style\\":\\"list\\",\\"page\\":1,\\"n\\":48,\\"q\\":\\"%E7%BB%87%E8%BF%B9\\",\\"tab\\":\\"all\\",\\"pageSize\\":48,\\"totalPage\\":100,\\"totalResults\\":4800,\\"sourceS\\":\\"0\\",\\"sort\\":\\"_coefp\\",\\"bcoffset\\":\\"\\",\\"ntoffset\\":\\"\\",\\"filterTag\\":\\"\\",\\"service\\":\\"\\",\\"prop\\":\\"\\",\\"loc\\":\\"\\",\\"start_price\\":null,\\"end_price\\":null,\\"itemIds\\":null,\\"p4pIds\\":null}"}'
    var document_cookie= cookie
    var n_data = n_param
    function token(e= '_m_h5_tk') {
        var t = new RegExp("(?:^|;\\s*)" + e + "\\=([^;]+)(?:;\\s*|$)").exec(document_cookie);
        return t ? t[1].split("_")[0] : void 0
    }
    function u(e) {
        function t(e, t) {
            return e << t | e >>> 32 - t
        }
        function n(e, t) {
            var n, r, o, i, a;
            return o = 2147483648 & e,
            i = 2147483648 & t,
            a = (1073741823 & e) + (1073741823 & t),
            (n = 1073741824 & e) & (r = 1073741824 & t) ? 2147483648 ^ a ^ o ^ i : n | r ? 1073741824 & a ? 3221225472 ^ a ^ o ^ i : 1073741824 ^ a ^ o ^ i : a ^ o ^ i
        }
        function r(e, t, n) {
            return e & t | ~e & n
        }
        function o(e, t, n) {
            return e & n | t & ~n
        }
        function i(e, t, n) {
            return e ^ t ^ n
        }
        function a(e, t, n) {
            return t ^ (e | ~n)
        }
        function s(e, o, i, a, s, u, l) {
            return e = n(e, n(n(r(o, i, a), s), l)),
            n(t(e, u), o)
        }
        function u(e, r, i, a, s, u, l) {
            return e = n(e, n(n(o(r, i, a), s), l)),
            n(t(e, u), r)
        }
        function l(e, r, o, a, s, u, l) {
            return e = n(e, n(n(i(r, o, a), s), l)),
            n(t(e, u), r)
        }
        function c(e, r, o, i, s, u, l) {
            return e = n(e, n(n(a(r, o, i), s), l)),
            n(t(e, u), r)
        }
        function f(e) {
            for (var t, n = e.length, r = n + 8, o, i = 16 * ((r - r % 64) / 64 + 1), a = new Array(i - 1), s = 0, u = 0; n > u; )
                s = u % 4 * 8,
                a[t = (u - u % 4) / 4] = a[t] | e.charCodeAt(u) << s,
                u++;
            return s = u % 4 * 8,
            a[t = (u - u % 4) / 4] = a[t] | 128 << s,
            a[i - 2] = n << 3,
            a[i - 1] = n >>> 29,
            a
        }
        function d(e) {
            var t, n, r = "", o = "";
            for (n = 0; 3 >= n; n++)
                r += (o = "0" + (t = e >>> 8 * n & 255).toString(16)).substr(o.length - 2, 2);
            return r
        }
        function p(e) {
            e = e.replace(/\r\n/g, "\n");
            for (var t = "", n = 0; n < e.length; n++) {
                var r = e.charCodeAt(n);
                128 > r ? t += String.fromCharCode(r) : r > 127 && 2048 > r ? (t += String.fromCharCode(r >> 6 | 192),
                t += String.fromCharCode(63 & r | 128)) : (t += String.fromCharCode(r >> 12 | 224),
                t += String.fromCharCode(r >> 6 & 63 | 128),
                t += String.fromCharCode(63 & r | 128))
            }
            return t
        }
        var h, m, y, v, g, A, b, _, w, M = [], S = 7, x = 12, k = 17, L = 22, E = 5, C = 9, T = 14, O = 20, Y = 4, D = 11, j = 16, P = 23, I = 6, B = 10, N = 15, R = 21, F;
        for (M = f(e = p(e)),
        A = 1732584193,
        b = 4023233417,
        _ = 2562383102,
        w = 271733878,
        h = 0; h < M.length; h += 16)
            m = A,
            y = b,
            v = _,
            g = w,
            A = s(A, b, _, w, M[h + 0], 7, 3614090360),
            w = s(w, A, b, _, M[h + 1], x, 3905402710),
            _ = s(_, w, A, b, M[h + 2], k, 606105819),
            b = s(b, _, w, A, M[h + 3], L, 3250441966),
            A = s(A, b, _, w, M[h + 4], 7, 4118548399),
            w = s(w, A, b, _, M[h + 5], x, 1200080426),
            _ = s(_, w, A, b, M[h + 6], k, 2821735955),
            b = s(b, _, w, A, M[h + 7], L, 4249261313),
            A = s(A, b, _, w, M[h + 8], 7, 1770035416),
            w = s(w, A, b, _, M[h + 9], x, 2336552879),
            _ = s(_, w, A, b, M[h + 10], k, 4294925233),
            b = s(b, _, w, A, M[h + 11], L, 2304563134),
            A = s(A, b, _, w, M[h + 12], 7, 1804603682),
            w = s(w, A, b, _, M[h + 13], x, 4254626195),
            _ = s(_, w, A, b, M[h + 14], k, 2792965006),
            A = u(A, b = s(b, _, w, A, M[h + 15], L, 1236535329), _, w, M[h + 1], 5, 4129170786),
            w = u(w, A, b, _, M[h + 6], 9, 3225465664),
            _ = u(_, w, A, b, M[h + 11], T, 643717713),
            b = u(b, _, w, A, M[h + 0], O, 3921069994),
            A = u(A, b, _, w, M[h + 5], 5, 3593408605),
            w = u(w, A, b, _, M[h + 10], 9, 38016083),
            _ = u(_, w, A, b, M[h + 15], T, 3634488961),
            b = u(b, _, w, A, M[h + 4], O, 3889429448),
            A = u(A, b, _, w, M[h + 9], 5, 568446438),
            w = u(w, A, b, _, M[h + 14], 9, 3275163606),
            _ = u(_, w, A, b, M[h + 3], T, 4107603335),
            b = u(b, _, w, A, M[h + 8], O, 1163531501),
            A = u(A, b, _, w, M[h + 13], 5, 2850285829),
            w = u(w, A, b, _, M[h + 2], 9, 4243563512),
            _ = u(_, w, A, b, M[h + 7], T, 1735328473),
            A = l(A, b = u(b, _, w, A, M[h + 12], O, 2368359562), _, w, M[h + 5], 4, 4294588738),
            w = l(w, A, b, _, M[h + 8], D, 2272392833),
            _ = l(_, w, A, b, M[h + 11], j, 1839030562),
            b = l(b, _, w, A, M[h + 14], P, 4259657740),
            A = l(A, b, _, w, M[h + 1], 4, 2763975236),
            w = l(w, A, b, _, M[h + 4], D, 1272893353),
            _ = l(_, w, A, b, M[h + 7], j, 4139469664),
            b = l(b, _, w, A, M[h + 10], P, 3200236656),
            A = l(A, b, _, w, M[h + 13], 4, 681279174),
            w = l(w, A, b, _, M[h + 0], D, 3936430074),
            _ = l(_, w, A, b, M[h + 3], j, 3572445317),
            b = l(b, _, w, A, M[h + 6], P, 76029189),
            A = l(A, b, _, w, M[h + 9], 4, 3654602809),
            w = l(w, A, b, _, M[h + 12], D, 3873151461),
            _ = l(_, w, A, b, M[h + 15], j, 530742520),
            A = c(A, b = l(b, _, w, A, M[h + 2], P, 3299628645), _, w, M[h + 0], 6, 4096336452),
            w = c(w, A, b, _, M[h + 7], B, 1126891415),
            _ = c(_, w, A, b, M[h + 14], N, 2878612391),
            b = c(b, _, w, A, M[h + 5], R, 4237533241),
            A = c(A, b, _, w, M[h + 12], 6, 1700485571),
            w = c(w, A, b, _, M[h + 3], B, 2399980690),
            _ = c(_, w, A, b, M[h + 10], N, 4293915773),
            b = c(b, _, w, A, M[h + 1], R, 2240044497),
            A = c(A, b, _, w, M[h + 8], 6, 1873313359),
            w = c(w, A, b, _, M[h + 15], B, 4264355552),
            _ = c(_, w, A, b, M[h + 6], N, 2734768916),
            b = c(b, _, w, A, M[h + 13], R, 1309151649),
            A = c(A, b, _, w, M[h + 4], 6, 4149444226),
            w = c(w, A, b, _, M[h + 11], B, 3174756917),
            _ = c(_, w, A, b, M[h + 2], N, 718787259),
            b = c(b, _, w, A, M[h + 9], R, 3951481745),
            A = n(A, m),
            b = n(b, y),
            _ = n(_, v),
            w = n(w, g);
        return (d(A) + d(b) + d(_) + d(w)).toLowerCase()
    }
    var time_1 = (new Date).getTime()
    var sign = u(token() + "&" +  time_1 + "&" + '12574478' + "&" + n_data)

    console.log(time_1, sign)
    return {'time':time_1,'sign':sign}
}
get_timeandsign(1,1)