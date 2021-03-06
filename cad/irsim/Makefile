# Created by: swallace
# $FreeBSD$

PORTNAME=	irsim
PORTVERSION=	9.7.89
CATEGORIES=	cad
MASTER_SITES=	http://opencircuitdesign.com/irsim/archive/
EXTRACT_SUFX=	.tgz

MAINTAINER=	danilo@FreeBSD.org
COMMENT=	Event-driven logic-level simulator for MOS circuis

LICENSE=	GPLv2

OPTIONS_RADIO=	INTERPRETER
OPTIONS_RADIO_INTERPRETER=	SCHEME TCL
OPTIONS_DEFAULT=	SCHEME
SCHEME_DESC=	Scheme interpreter
TCL_DESC=	Tcl interpreter
OPTIONS_SUB=	yes

SCHEME_CONFIGURE_ON=	--with-interpreter=scheme
TCL_CONFIGURE_ON=	--with-interpreter=tcl --with-tcl=${TCL_LIBDIR} \
			--with-tk=${TK_LIBDIR} --with-tclincls=${TCL_INCLUDEDIR} \
			--with-tkincls=${TK_INCLUDEDIR} --with-tcllibs=${LOCALBASE}/lib \
			--with-tklibs=${LOCALBASE}/lib

CONFIGURE_WRKSRC=	${WRKSRC}/scripts

USES=	gmake
USE_XORG=	x11
GNU_CONFIGURE=	yes

CFLAGS+=	-I${LOCALBASE}/include
LDFLAGS+=	-L${LOCALBASE}/lib

.include <bsd.port.options.mk>

.if ${PORT_OPTIONS:MTCL}
USES+=	tk
PLIST_SUB+=	NOTCL="@comment "
.else
WISH=		${FALSE}
PLIST_SUB+=	NOTCL=""
.endif

.if empty(PORT_OPTIONS:MSCHEME) && empty(PORT_OPTIONS:MTCL)
CONFIGURE_ARGS+=	--with-interpreter=no
.endif

post-patch:
	@${REINPLACE_CMD} -e \
		's|FreeBSD-\*|*-*-freebsd*| ; \
		 s|wish |${WISH:T} | ; \
		 s|"-fpic"|"-fPIC"| ; \
		 /-l\/usr\/X11R6\/include/d' ${CONFIGURE_WRKSRC}/configure

.include <bsd.port.mk>
