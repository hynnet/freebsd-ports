# Created by: Michael Johnson <ahze@ahze.net>
# $FreeBSD$

PORTNAME=	ExtUtils-MakeMaker
PORTVERSION=	7.04
CATEGORIES=	devel perl5
MASTER_SITES=	CPAN
PKGNAMEPREFIX=	p5-

MAINTAINER=	perl@FreeBSD.org
COMMENT=	Designed to write a Makefile for an extension module

LICENSE=	ART10 GPLv1
LICENSE_COMB=	dual

USES=		perl5
USE_PERL5=	configure

.include <bsd.port.pre.mk>

.if ${PERL_LEVEL} < 501600
BUILD_DEPENDS+=	p5-CPAN-Meta>=2.113640:${PORTSDIR}/devel/p5-CPAN-Meta
RUN_DEPENDS+=	p5-CPAN-Meta>=2.113640:${PORTSDIR}/devel/p5-CPAN-Meta
.endif

.if ${PERL_LEVEL} < 501800
BUILD_DEPENDS+=	p5-CPAN-Meta-Requirements>=2.121:${PORTSDIR}/devel/p5-CPAN-Meta-Requirements
RUN_DEPENDS+=	p5-CPAN-Meta-Requirements>=2.121:${PORTSDIR}/devel/p5-CPAN-Meta-Requirements
.endif

post-patch:
	@${REINPLACE_CMD} -e '/EXE_FILES/d; /my::bundles/d' ${WRKSRC}/Makefile.PL
	@${REINPLACE_CMD} -e '/^bundled\//d' ${WRKSRC}/MANIFEST
	@${RM} -fr ${WRKSRC}/bundled/

.include <bsd.port.post.mk>
