# Created by: Yoshisato YANAGISAWA <osho@pcc-software.org>
# $FreeBSD$

PORTNAME=	camellia
PORTVERSION=	1.2
CATEGORIES=	security ruby
MASTER_SITES=	http://info.isl.ntt.co.jp/crypt/camellia/dl/
PKGNAMEPREFIX=	${RUBY_PKGNAMEPREFIX}
DISTNAME=	${PORTNAME}-rb-${PORTVERSION}
DIST_SUBDIR=	ruby

MAINTAINER=	osho@pcc-software.org
COMMENT=	Ruby extension library which implements Camellia encryption

USE_RUBY=	yes
USE_RUBY_SETUP=	yes

INSTALL_TARGET=	site-install

DOCS=		README.txt History.txt License.txt
EXAMPLES=	ext/camellia-example.rb

OPTIONS_DEFINE=	DOCS

post-install:
	${MKDIR} ${STAGEDIR}${RUBY_MODEXAMPLESDIR}
.for f in ${EXAMPLES}
	${INSTALL_DATA} ${WRKSRC}/${f} ${STAGEDIR}${RUBY_MODEXAMPLESDIR}/
.endfor
	${MKDIR} ${STAGEDIR}${RUBY_MODDOCDIR}
.for f in ${DOCS}
	${INSTALL_DATA} ${WRKSRC}/${f} ${STAGEDIR}${RUBY_MODDOCDIR}/
.endfor

.include <bsd.port.pre.mk>

.if ${RUBY_VER} == 2.1
BROKEN=		Does not build with Ruby 2.1
.endif

.include <bsd.port.post.mk>
