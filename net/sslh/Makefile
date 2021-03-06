# Created by: Jui-Nan Lin <jnlin@csie.nctu.edu.tw>
# $FreeBSD$

PORTNAME=	sslh
PORTVERSION=	1.16
DISTVERSIONPREFIX=	v
PORTREVISION=	2
CATEGORIES=	net
MASTER_SITES=	http://www.rutschle.net/tech/

MAINTAINER=	olivier@cochard.me
COMMENT=	SSL/SSH multiplexer

LICENSE=	GPLv2

LIB_DEPENDS=	libconfig.so:${PORTSDIR}/devel/libconfig

USES=		gmake perl5
USE_PERL5=	build

OPTIONS_DEFINE=	EXAMPLES LIBWRAP
OPTIONS_DEFAULT=	EXAMPLES LIBWRAP

CFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib

PLIST_FILES=	sbin/sslh-fork \
		sbin/sslh-select \
		etc/sslh.conf.sample \
		man/man8/sslh.8.gz

USE_RC_SUBR=	sslh

PORTEXAMPLES=	example.cfg

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MLIBWRAP}
MAKE_ENV+=	USELIBWRAP=1
.endif

post-patch:
	@${REINPLACE_CMD} -Ee 's,^(release=)$$,\1${PORTVERSION},' \
		${WRKSRC}/genver.sh
	@${REINPLACE_CMD} -Ee 's,/etc/init.d/(sslh),${PREFIX}/etc/rc.d/\1,g; \
		s,/etc/default/(sslh),${PREFIX}/etc/\1.conf,g' \
		${WRKSRC}/sslh.pod

do-install:
	${INSTALL_PROGRAM} ${WRKSRC}/sslh-fork ${STAGEDIR}${PREFIX}/sbin
	${INSTALL_PROGRAM} ${WRKSRC}/sslh-select ${STAGEDIR}${PREFIX}/sbin
	${INSTALL_DATA} ${WRKSRC}/basic.cfg \
		${STAGEDIR}${PREFIX}/etc/${PORTNAME}.conf.sample
	${INSTALL_MAN} ${WRKSRC}/sslh.8.gz ${STAGEDIR}${MANPREFIX}/man/man8
	@${MKDIR} ${STAGEDIR}${EXAMPLESDIR}
	${INSTALL_DATA} ${PORTEXAMPLES:S,^,${WRKSRC}/,} \
		${STAGEDIR}${EXAMPLESDIR}/

.include <bsd.port.mk>
